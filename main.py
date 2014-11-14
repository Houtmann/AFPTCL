# -*- coding: utf-8 -*-
# By hadmagic test
# This file is part of AFPT.

# AFPT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AFPT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AFPT.  If not, see <http://www.gnu.org/licenses/>
# You can read the license.txt in parent directory

import os
import argparse
import threading
import scripts
import sys



scripts.make_dir() #Create folder
scripts.create_log() #Create logs text files
scripts.index_css() #Create a CSS file for reports


list_fonction = [scripts.search_jpeg, scripts.search_gif,
                 scripts.search_png, scripts.search_docs,
                 scripts.search_pdf, scripts.search_videos,
                 scripts.search_tiff]

if 'win' in sys.platform:
    clear = lambda: os.system('cls')
    clear()
else:
    clear = lambda: os.system('clear')
    clear()

print('==========================================================')
print('============            AFPT  v1.0            ============ ')
print('==========================================================')
print('')
print('''usage: main.py [-h] [-p PATH] [-cv] [-sf] [-hash] [-e EXIF]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  start a disk scan of path, precise path of disk
  -cv                   Copy videos files in tmp dir
  -sf                   Don't search files in disk(images, docs, videos etc...
  -hash                 Hash all files of the disk and store it in sqlite3 db
  -e EXIF, --exif EXIF  Get exif informations on specified jpeg image
''')

#Arguments parser#
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", action = 'store', help="start a disk scan of path, precise path of disk")
parser.add_argument("-cv",action = "store_true",
                                    help="Copy videos files in tmp dir")
parser.add_argument("-sf",action = "store_false",
                                    help="Don't search files in disk(images, docs, videos etc...")
parser.add_argument("-hash",action = "store_true",
                                    help="Hash all files of the disk and store it in sqlite3 db")
parser.add_argument("-e", "--exif" ,action = "store",
                                    help="Get exif informations on specified jpeg image")
args = parser.parse_args()



if args.path:
    print('Starting disk scan...')
    print('')
    print('Creating log_tree.txt in {0}/tmp/ ...'.format(os.path.abspath('.')))
    scripts.scan(args.path) #Complete scan of disk"

    if args.hash:
        print('\n'+'Hashing file...')
        scripts.create_db()
        scripts.hash_all()

    print('')
    print('')

                 
    if args.sf:
        print('Search  files...')
        print('')
        print('Jpg, gif, png, docs, videos etc...')
        print('')
        print('Creating log_, in {0}/tmp/ ...'.format(os.path.abspath('.')))
        print('')
        for i in list_fonction:
            i = threading.Thread(target=i, args=(args.cv,))
            i.start()
        i.join()

if args.path:
    print('Forensics Mozilla Firefox...')
    print('')
    print('Creating moz_ccokies.html and moz_forms.html in {0}/tmp/ ...'.format(os.path.abspath('.')))

    scripts.moz_cookies()
    scripts.moz_form()

    print('')
    print('')
    print('Forensics Windows registry...')
    print('')
    print('')
    print('Creating registre.html in {0}/tmp/ ...'.format(os.path.abspath('.')))


    scripts.boot(args.path)
    scripts.boot_2(args.path)
    scripts.usb_1(args.path)
    scripts.make_log()

if args.cv:
    #copy_files()
    print('')
    print('')

if args.exif:
    scripts.get_exif(args.exif)
#clear()




os.system('pause')









