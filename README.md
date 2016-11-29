[![Stories in Ready](https://badge.waffle.io/ArthurMoore85/romulus.png?label=ready&title=Ready)](https://waffle.io/ArthurMoore85/romulus)
[![Build Status](https://travis-ci.org/ArthurMoore85/romulus.svg?branch=master)](https://travis-ci.org/ArthurMoore85/romulus)
[![Code Health](https://landscape.io/github/ArthurMoore85/romulus/master/landscape.svg?style=flat)](https://landscape.io/github/ArthurMoore85/romulus/master)

# Romulus
Linux Retropie manager

Managing your Retropie shouldn't be difficult, that's why there's Romulus.
Romulus acts as the middleman between your Retropie, and Linux machine.
It allows you to search for, and download ROMs, connect to your Raspberry Pi, and send your ROMs to the Pi.

All from one app.

Features:
* Automatic Pi detection
* Searching ROMs through Emuparadise
* Pi Status (Online/Offline)
* ROM downloading
* Syncing ROMs with Pi (sending local ROMs to Pi)
* View local games library
* View Retropie's remote library

Details
-------
Romulus is written using Python 2.7.
For it's GUI framework it makes use of PyQt.
See the requirements.txt file for information on required libraries.

Installation
------------
In order to run this app, you will require PyQt4.
Find PyQt4 in your package manager:

_Ubuntu_: `sudo apt-get install python-pip python2.7-dev libxext-dev python-qt4 qt4-dev-tools build-essential`

_Fedora 21_: `sudo yum install PyQt4-devel`

_Fedora 22+_: `sudo dnf install PyQt4-devel`

The solution above is the not-so-great installation. You should be using a virtualenv and install everything through there. But alas, I did not. 
[If you decide to do it the right way, I suggest following these instructions](http://movingthelamppost.com/blog/html/2013/07/12/installing_pyqt____because_it_s_too_good_for_pip_or_easy_install_.html)

Once installed, install the requirements using the command `pip install -r requirements.txt`

Developers
----------
All code is licensed under GNU Public License 2 (GPLv2). This license allows you to copy, edit, and redistribute without restriction, as long as it retains the free GPLv2 license.

All help is appreciated, whether filing bug reports, squashing bugs, requesting features or anything else, simply clone this repo, and if you have improved it somehow, make a pull request.

Authors
-------
Arthur Moore <arthur.moore85@gmail.com>
