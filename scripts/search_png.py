
import os
import sys
import glob
import shutil



def search_png(arg):
    
    sign = b'PNG' #Signature
    tree_txt = open('tmp/log_tree.txt', 'r')
    
    for i in tree_txt.readlines():
            if i:
                    try:
                        file = open(i.strip('\n'), 'rb', buffering = 1)
                        if sign  in file.read(5):
                            log_file = open('tmp/log_PNG.txt', 'a')
                            log_file.write(i)
                            log_file.close()
                        file.close()
                    except:
                        pass
    tree_txt.close()
                                      
    
    if arg:
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
                
