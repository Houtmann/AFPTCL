
import os
import sys
import binascii
import time
import pdb
import threading
import queue
from queue import *
from tempfile import mkstemp

def sumfile(filePath):
	fileObj = open(filePath, 'rb')
	m = hashlib.md5()
	while True:
		d = fileObj.read(50000)
		if not d:
			break
		m.update(d)
	return m.hexdigest()

def search_videos():
     
    print('')
    print('')
    print('Recherche de fichier videos par signature hexadecimal')
    print('')
    print('')
    input(' Appuyez sur une touche pour continuer ')
    
    sign = [b'RIFF',
            b'\x00\x00\x00 ftypisom' ,
            b'\x1aE\xdf\xa3\xa3B\x86\x81\x01B\xf7\x81\x01B\xf2']
    
    
    list_file = []
    
    print('')
    print('Recherche en cours...')
    tree_txt = open('log_tree.txt', 'r')
    for i in tree_txt.readlines():
            if i:
                    try:
                        file = open(i.strip('\n'), 'rb+', buffering=500)
                        for o in sign:
                            if o  in file.read(15):
                                list_file.append(i)
                                log_file = open('log_videos.txt', 'a')
                                log_file.write(i)
                    except:
                        pass
                    
            
                                      
    result = open('log_videos.txt', 'r')                  

    for a in result:
        dest = '/tmp/videos/' #Dossier de destination des liens sym 
        if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier images
                
        elif 'win' in sys.platform:
                tempath = os.path.realpath(__file__)
                dest2 = tempath.strip('scripts\search_videos_etwav.py')
                dest3 = '\\tmp\\jpg\\'
                
                shutil.copy(a.strip('\n'), dest2 + dest3 )
