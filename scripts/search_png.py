
import os
import sys
import binascii
import time
import pdb
import glob
import shutil
import os.path


def search_png():
    sign = b'PNG' #Signature
    list_file = []
    
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
            if i:
                    try:
                        file = open(i.strip('\n'), 'rb+', buffering=500)
                        if sign  in file.read(5):
                            list_file.append(i)
                            log_file = open('tmp/log_PNG.txt', 'a')
                            log_file.write(i)
                    except:
                        pass
                    
            
                                      
    result = open('tmp/log_PNG.txt', 'r')                  
    for a in result:
        dest = '/tmp/png/' #Dossier de destination des liens sym pour les JPEG
        if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier images
                
        elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\png\\'
                shutil.copy(a.strip('\n'), dest2 + dest3 )
                