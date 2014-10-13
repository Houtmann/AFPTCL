# -*- coding: utf-8 -*-
import os
from datetime import datetime
from scripts.scan import scan
from scripts.search_jpeg import search_jpeg
from scripts.search_gif import search_gif
from scripts.search_png import search_png
from scripts.search_doc import search_doc
from scripts.search_pdf import search_pdf
from scripts.listdisks import *
from scripts.registre import *
from scripts.moz_cookies import moz_cookies
from scripts.moz_form import moz_form
from scripts.copy_files import copy_files
from scripts.search_videos import search_videos
import sys
import argparse
import time

def make_dir():
    path = os.path.abspath('.')
    print(path)
    try:
        os.mkdir(path + '\\tmp')
        tmp = path + '\\tmp'
        os.mkdir(tmp + '\\jpg')
        os.mkdir(tmp + '\\gif')
        os.mkdir(tmp + '\\docs')
        os.mkdir(tmp + '\\videos')
        os.mkdir(tmp + '\\pdf')
        os.mkdir(tmp + '\\png')
    except:
        pass
make_dir()

def create_log(): #create txt files log
    create_tree = open(os.path.abspath('.') + '\\tmp\\log_tree.txt', 'w')
    create_jpg = open(os.path.abspath('.') + '\\tmp\\log_jpg.txt', 'w')
    create_gif = open(os.path.abspath('.') + '\\tmp\\log_gif.txt', 'w')
    create_png = open(os.path.abspath('.') + '\\tmp\\log_png.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_docs.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_pdf.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_videos.txt', 'w')
    
create_log()

clear = lambda: os.system('cls')

clear()
print('==========================================================')
print('=====                 AFPT  v1.0                     =====')
print('==========================================================')
print('')
print('')

#Arguments parser#
parser = argparse.ArgumentParser()
parser.add_argument("p", help="precise path of disk")
parser.add_argument("-cv",action = "store_true",
                                    help="Copy videos files in tmp dir")
args = parser.parse_args()

print('Starting disk scan...')
print('')
print('Creating log_tree.txt in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

#scan(args.p) #Complete scan of disk

print('')
print('')
print('Search pictures files...')
print('')
print('Creating log_jpg, log_gif, log_png in {0}\\tmp\\ ...'.format(os.path.abspath('.')))
print('')

#search_jpeg()
#search_gif()
#search_png()

print('')
print('')
print('Search documents files...')
print('')
print('Creating log_docs.txt in {0}\\tmp\\ ...'.format(os.path.abspath('.')))

#search_doc()
#search_pdf()
print('')
print('')
print('Search videos files...')
print('Creating log_videos.txt in {0}\\tmp\\ ...'.format(os.path.abspath('.')))
#search_videos()
if args.cv:
    copy_files()
print('')
print('')
print('Forensics Mozilla Firefox...')
print('')
print('Creating moz_ccokies.html and moz_forms.html in {0}\\tmp\\ ...'.format(os.path.abspath('.')))                                                                        
moz_cookies()
moz_form()
print('')
print('')
print('Forensics Windows registry...')
print('')
print('Creating registre.html in {0}\\tmp\\ ...'.format(os.path.abspath('.')))                                                                               
boot(args.p)

os.system('pause')









