# -*- coding: utf-8 -*-

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

"""from scripts.scan import scan
from scripts.search_jpeg import search_jpeg
from scripts.search_gif import search_gif
from scripts.search_png import search_png
from scripts.search_docs import search_docs
from scripts.search_pdf import search_pdf
#from scripts.listdisks import *
from scripts.registre import *
from scripts.moz_cookies import moz_cookies
from scripts.moz_form import moz_form
from scripts.copy_files import copy_files
from scripts.search_videos import search_videos
from scripts.index_css import index_css
from scripts.make_log import make_log
from scripts.init_folder_files import *
from scripts.search_moffice import search_moffice
from scripts.hash_all import *"""
import os
import argparse
import threading
import scripts



scripts.make_dir() #Create folder
scripts.create_log() #Create logs text files
scripts.index_css() #Create a CSS file for reports


list_fonction = [scripts.search_jpeg, scripts.search_gif,scripts.search_png, scripts.search_docs,
                 scripts.search_pdf, scripts.search_videos]

clear = lambda: os.system('cls')
clear()

print('==========================================================')
print('============            AFPT  v1.0            ============ ')
print('==========================================================')
print('')
print('')

#Arguments parser#
parser = argparse.ArgumentParser()

parser.add_argument("p", help="precise path of disk")

parser.add_argument("-cv",action = "store_true",
                                    help="Copy videos files in tmp dir")

parser.add_argument("-sf",action = "store_false",
                                    help="Don't search files in disk")
parser.add_argument("-hash",action = "store_true",
                                    help="Hash all files of the disk and store it in sqlite3 db")
args = parser.parse_args()



print('Starting disk scan...')
print('')
print('Creating log_tree.txt in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

scripts.scan(args.p) #Complete scan of disk"

if args.hash:
    print('Hashing file...')
    scripts.create_db()
    scripts.hash_all()

print('')
print('')

                 
if args.sf:
    print('Search  files...')
    print('')
    print('Jpg, gif, png, docs, videos etc...')
    print('')
    print('Creating log_, in {0}\\tmp\\ ...'.format(os.path.abspath('.')))
    print('')
    for i in list_fonction:
        i = threading.Thread(target=i, args=(args.cv,))
        i.start()
    i.join()
        
if args.cv:
    #copy_files()
    print('')
    print('')
    
clear()

print('Forensics Mozilla Firefox...')
print('')
print('Creating moz_ccokies.html and moz_forms.html in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

scripts.moz_cookies()
scripts.moz_form()

print('')
print('')
print('Forensics Windows registry...')
print('')
print('')
print('Creating registre.html in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

scripts.user(args.p)
scripts.boot(args.p)
scripts.boot_2(args.p)
scripts.usb_1(args.p)
scripts.make_log()



os.system('pause')









