
import os
import sys
import binascii
import time
import pdb
import shutil

def search_pdf(arg):
     
    sign = b'%PDF' #Signature
    
    tree_txt = open('tmp/log_tree.txt', 'r')
    
    for i in tree_txt.readlines():
            if i:
                    try:
                        file = open(i.strip('\n'), 'rb+')
                        if sign  in file.read(4):
                            log_file = open('tmp/log_pdf.txt', 'a')
                            log_file.write(i)
                            
                    except:
                        pass
    tree_txt.close()                                                
    
    if arg == True:
        result = open('tmp/log_PDF.txt', 'r')
        for a in result:
            dest = '/tmp/jpg/' #Dossier de destination des liens sym pour les JPEG
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier images
                
            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\jpg\\'
                shutil.copy(a.strip('\n'), dest2 + dest3 )
    
