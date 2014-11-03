# -*- coding: utf-8 -*-
import os
from datetime import datetime
from scripts.scan import scan
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
import sys
import argparse
import time
import threading


        
make_dir() #Create folder
create_log() #Create logs text files
index_css() #Create a CSS file for reports

list_fonction = [search_jpeg, search_gif,search_png, search_docs,
                 search_pdf, search_videos]

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
args = parser.parse_args()



print('Starting disk scan...')
print('')
print('Creating log_tree.txt in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

scan(args.p) #Complete scan of disk

print('')
print('')
print('Search  files...')
print('')
print('Jpg, gif, png, docs, videos etc...')
print('')
print('Creating log_, in {0}\\tmp\\ ...'.format(os.path.abspath('.')))
print('')
                 
if args.sf:
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

moz_cookies()
moz_form()

print('')
print('')
print('Forensics Windows registry...')
print('')
print('')
print('Creating registre.html in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

user(args.p)
boot(args.p)
boot_2(args.p)
usb_1(args.p)
make_log()



os.system('pause')









