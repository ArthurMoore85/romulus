"""
:module: emuparadise.py
:description: Scraper for Emuparadise by Fopina.

:url: https://codegists.com/snippet/python/emuparadisepy_fopina_python
:author: Fopina
:edited by: Arthur Moore <arthur.moore85@gmail.com>
:date collected: 26/11/16
"""
import requests
import re
import HTMLParser
from urlparse import urljoin

BASE_URL = 'http://www.emuparadise.me/'


class EmuParadise(object):
    referer = None
    h = HTMLParser.HTMLParser()

    def get_link(self, game_url):
        links = re.findall(
            '<a href="(/roms/get-download.php?.*?)" id="download-link"',
            self._get(game_url + '-download').content
        )
        if links:
            return self._get(self.h.unescape(links[0]), follow=False).headers['location']

    def search(self, query, system=0):
        return re.findall(
            '<div class="roms"><a .*?href="(.*?)">(.*?)</a>.*?<a href="\/roms\/roms\.php'
            '\?sysid=(\d+)".*?class="sysname">(.*?)</a>.*?<b>Size:</b> (.*?) .*?</div>',
            self._get(
                '/roms/search.php',
                data=dict(query=query, section='roms', sysid=system)
            ).content
        )

    def _get(self, url, follow=True, data=None):
        url = urljoin(BASE_URL, url)
        extra = dict(cookies=dict(downloadcaptcha='1'))
        if self.referer is not None:
            extra['headers'] = dict(referer=self.referer)
        if not follow:
            extra['allow_redirects'] = False
        if data is not None:
            extra['params'] = data
        self.referer = url
        return requests.get(url, **extra)
