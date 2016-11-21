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
* ROM downloading (not yet implemented)
* Syncing ROMs with Pi (not yet implemented)

Details
-------
Romulus is written using Python 2.7.
For it's GUI framework it makes use of PyQt.
See the requirements.txt file for information on required libraries.

Installation
------------
In order to run this app, you will require PyQt4.
Find PyQt4 in your package manager:

_Ubuntu_: `sudo apt-get install pyqt4-dev-tools`

_Fedora 21_: `sudo yum install PyQt4-devel`

_Fedora 22+_: `sudo dnf install PyQt4-devel`

Once installed, install the requirements using the command `sudo pip install -r requirements.txt`

Developers
----------
All code is licensed under GNU Public License 2 (GPLv2). This license allows you to copy, edit, and redistribute without restriction, as long as it retains the free GPLv2 license.
There will also be an API available.
