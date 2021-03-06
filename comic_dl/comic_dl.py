#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __version__ import __version__
import argparse
import logging
import sys
import platform
import honcho
import os
import time


class ComicDL(object):
    def __init__(self, argv):
        parser = argparse.ArgumentParser(description='Comic_dl is a command line tool to download comics and manga '
                                                     'from various such sites.')

        parser.add_argument('--version', action='store_true', help='Shows version and exits.')
        parser.add_argument('-s', '--sorting', nargs=1, help='Decides downloading order of chapters.')
        parser.add_argument('-dd', '--download-directory', nargs=1, help='Decides the download directory of the comics/manga.')
        parser.add_argument('-rn', '--range', nargs=1, help='Specifies the range of chapters to download.', default='All')
        parser.add_argument('--convert', nargs=1, help='Tells the script to convert the downloaded Images to PDF or anything else.')
        parser.add_argument('--keep', nargs=1, help='Tells the script whether to keep the files after conversion or not.', default='True')
        parser.add_argument('--quality', nargs=1,
                            help='Tells the script which Quality of image to download (High/Low).', default='True')

        parser.add_argument('-i', '--input', nargs=1, help='Inputs the URL to anime.')

        parser.add_argument("-v", "--verbose", help="Prints important debugging messages on screen.",
                            action="store_true")
        logger = False

        args = parser.parse_args()

        if args.version:
            self.version()
            sys.exit()

        if args.verbose:
            print("\n***Starting the script in Verbose Mode***\n")
            try:
                os.remove("Error_Log.log")
            except:
                pass
            logging.basicConfig(format='%(levelname)s: %(message)s', filename="Error_Log.log", level=logging.DEBUG)
            logging.debug("Arguments Provided : %s" % args)
            logging.debug("Operating System : %s - %s - %s" % (platform.system(),
                                                               platform.release(),
                                                               platform.version()
                                                               ))
            logging.debug("Python Version : %s (%s)" % (platform.python_version(), platform.architecture()[0]))
            logger = True

        if args.input is None:
            print("I need an Input URL to download from.")
            print("Run the script with --help to see more information.")
        else:
            if not args.sorting:
                args.sorting = ["ascending"]
            if not args.download_directory:
                args.download_directory = [os.getcwd()]
            if type(args.range) == list:
                args.range = args.range[0]
            if not args.convert:
                args.convert = ["None"]
            if not args.keep:
                args.keep = ["True"]
            if not args.quality:
                args.quality = ["Best"]

            start_time = time.time()
            honcho.Honcho().checker(comic_url=str(args.input[0]).strip(), current_directory=os.getcwd(),
                                    sorting_order=args.sorting[0], logger=logger, download_directory=args.download_directory[0], chapter_range=args.range, conversion=args.convert[0], delete_files=args.keep[0], image_quality=args.quality[0])
            end_time = time.time()
            total_time = end_time - start_time
            print("Total Time Taken To Complete : %s" % total_time)

    @staticmethod
    def version():
        print("Current Version : %s" % __version__)
