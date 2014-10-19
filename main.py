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
import sys
import argparse
import time
import threading

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
    create_css = open(os.path.abspath('.') + '\\index.css', 'w')
    create_tree = open(os.path.abspath('.') + '\\tmp\\log_tree.txt', 'w')
    create_jpg = open(os.path.abspath('.') + '\\tmp\\log_jpg.txt', 'w')
    create_gif = open(os.path.abspath('.') + '\\tmp\\log_gif.txt', 'w')
    create_png = open(os.path.abspath('.') + '\\tmp\\log_png.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_docs.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_pdf.txt', 'w')
    create_docs = open(os.path.abspath('.') + '\\tmp\\log_videos.txt', 'w')
    
create_log()
index_css()
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
    jpg = threading.Thread(target=search_jpeg, args=(args.cv,))
    gif = threading.Thread(target=search_gif, args=(args.cv,))
    png = threading.Thread(target=search_png, args=(args.cv,))
    docs = threading.Thread(target=search_docs, args=(args.cv,))
    pdf = threading.Thread(target=search_pdf, args=(args.cv,))
    videos = threading.Thread(target=search_videos)
    jpg.start()
    gif.start()
    png.start()
    docs.start()
    pdf.start()
    videos.start()
    #search_jpeg(args.cv)
    #search_gif(args.cv)
    #search_png(args.cv)
    #search_docs(args.cv)
    #search_pdf(args.cv)
    #search_videos()
    jpg.join()
    gif.join()
    png.join()
    docs.join()
    pdf.join()
    videos.join()

   
     
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

boot(args.p)
boot_2(args.p)
usb_1(args.p)
make_log()



os.system('pause')









