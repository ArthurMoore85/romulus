"""
:module: scraper.py
:description: Scrapes sites

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 20/11/16
"""
from __future__ import unicode_literals
import os
import textwrap
import urllib
import urllib2
import mechanize
from data.database import session, Settings
import imp
from bs4 import BeautifulSoup
from emuparadise import EmuParadise

__author__ = 'arthur'


class Scraper(object):
    def __init__(self, rom, parent=None):
        """
        Scrapes a website
        :param search_query: User search query
        """
        self.parent = parent
        self.session = session()
        self.url = None
        self.search_q = rom
        self.settings = self.get_settings
        self.browser = mechanize.Browser()

    @property
    def get_settings(self):
        """
        Retrieves user settings
        """
        loc = self.session.query(Settings).first().selected_service
        module = os.path.join(loc, 'settings.py')
        if os.path.isfile(module):
            settings = imp.load_source('*', module)
            self.url = settings.SITE.get('url', None)
            return settings
        else:
            raise AttributeError('Module is not a valid Romulus module')

    @property
    def homepage(self):
        """
        Returns homepage
        """
        response = self.browser.open(self.url)
        return response

    def fill_in_form(self):
        """
        Inserts data into the submit form
        :param form_name: Name of the form if available
        """
        self.browser.open(self.url)
        form_name = self.settings.SITE.get('search_form_name', None)
        if form_name:
            self.browser.select_form(form_name)
        else:
            self.browser.form = list(self.browser.forms())[0]
        input_field = self.settings.SITE.get('search_input_name')
        self.browser[input_field] = self.search_q
        html_return = self.browser.submit().read()
        res = self.handle_results(html_return)
        return res

    def handle_results(self, html_return):
        """
        Handles the results of the form
        :param html_return: HTML return of form
        """
        soup = BeautifulSoup(html_return, 'html.parser')
        class_name = self.settings.SITE.get('return_div_class')
        matches = soup.findAll('div', {'class': class_name})
        return matches

    def get_link(self, html):
        """
        Retrieves link for particular result
        :param html: html returned code
        """
        avoid_div_name = self.settings.SITE.get('avoid_link_div_name')
        links = html.findAll('a')
        element = self.settings.SITE.get('link_element')
        res = []
        for link in links:
            l = link.findAll(avoid_div_name)
            if len(l) < 1:
                res.append(link)
        return "{0}{1}".format(self.url, res[element]['href'])

    def get_description(self, url):
        """
        Gets description text
        """
        desc_text = self.settings.SITE.get('description_text')
        r = urllib2.Request(url)
        response = urllib2.urlopen(r)
        soup = BeautifulSoup(response, 'html.parser')
        matches = soup.findAll('div', {'class': desc_text})
        final_txt = self.reformat_description(matches[0].text)[8:]
        return final_txt

    def download_link(self, url):
        """
        Retrieves download url
        """
        emu = EmuParadise()
        link = emu.get_link(url)
        return link

    def reformat_description(self, description):
        """
        Reformats the description so it's viewable on Romulus
        """
        final_txt = '<br>'.join(textwrap.wrap(description, 40))
        return final_txt

    def _html_link_return(self, url, tag, key, value, deeper=False, second=False):
        """
        Returns links
        :param url: URL to filter
        :param key: Name of key to search in tag
        :param tag: Name of value to find
        :param value: Name of the value expected in tag
        """
        if url[0] == '/':
            url = '{0}{1}'.format(self.url, url)
        r = urllib2.Request(url)
        response = urllib2.urlopen(r)
        soup = BeautifulSoup(response, 'html.parser')
        matches = soup.findAll(tag, {key, value})
        if deeper:
            m = matches[0]
            matches = m.findAll('a')[0]['href']
        elif second:
            m = matches[0]
            matches = m.findAll('a')[1]['href']
            print m.findAll('a')
        else:
            matches = matches[0]['href']
        return '{0}{1}'.format(self.url, matches)

    def download(self, url, location):
        """
        In many cases such as Emuparadise, hotlinking is blocked.
        For that reason, we must follow the redirects with mechanize.
        After which we will download the file required.
        """
        link = self.download_link(url)
        file_name = urllib2.unquote(link.split('/')[-1])
        target_file_name = os.path.join(location, file_name)
        self.parent.status_signal.emit('Downloading {0}'.format(file_name))
        urllib.urlretrieve(link, target_file_name)
        f = urllib2.urlopen(link)
        data = f.read()
        with open(target_file_name, 'wb') as code:
            code.write(data)
        self.parent.status_signal.emit('Idle')
