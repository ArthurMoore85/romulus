"""
:module: compression.py
:description: Module for uncompressing various compressed files

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 09/12/16
"""
import os
import zipfile
import libarchive.public
from pyunpack import Archive

__author__ = 'arthur'


class Compression(object):
    def __init__(self, target):
        self.target_dir = target

    def determine_type(self, file_o):
        """
        Determines filetype, and requirements
        """
        file_type = os.path.splitext(file_o)[1][1:].lower()
        return file_o, file_type

    def unzip(self, file_obj):
        """
        Unzips a ZIP archive
        :param file_obj: file to be unzipped
        """
        zip_ref = zipfile.ZipFile(file_obj, 'r')
        zip_ref.extractall(self.target_dir)
        zip_ref.close()

    def unzip_seven(self, file_obj):
        """
        Extracts contents of 7z file
        :param file_obj: file to be used.
        """
        for entry in libarchive.public.file_pour(file_obj):
            continue

    def unrar(self, file_obj):
        """
        Extracts a RAR archive
        :param file_obj: file to be extracted.
        """
        Archive(file_obj).extractall(self.target_dir)

    def clean_up(self, file_o):
        """
        Cleans redundant archive file.
        """
        os.remove(file_o)

    def extract(self, file_o):
        """
        Extracts all files
        """
        f, t = self.determine_type(file_o)
        if t == 'zip':
            self.unzip(f)
        elif t == '7z':
            self.unzip_seven(f)
        elif t == 'rar':
            self.unrar(f)
        self.clean_up(file_o)
