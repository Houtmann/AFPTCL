import os
import sys
import glob
import shutil
import os.path


def search_jpeg(arg):
    
    jpeg = b'\xFF\xD8\xFF' #Signature du Jpeg
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
            if i:
                try:
                    file = open(i.strip('\n'), 'rb', buffering = 1)
                    
                    if jpeg in file.read(5):
                        log_jpg = open('tmp/log_jpg.txt', 'a')
                        log_jpg.write(i)
                        log_jpg.close()
                    file.close()
                except:
                    pass

    tree_txt.close()
    if arg == True:
        result = open('tmp/log_jpg.txt', 'r')
        for a in result:
            dest = '/tmp/jpg/' #Dossier de destination des liens sym pour les JPEG
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier images
                
            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\jpg\\'
                shutil.copy(a.strip('\n'), dest2 + dest3 )


    



