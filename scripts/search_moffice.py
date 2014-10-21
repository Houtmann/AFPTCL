import os
import sys
import glob
import shutil
import os.path


def search_moffice(arg):
    
    m_office = b'PK\x03\x04'
    
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
            if i:
                try:
                    file = open(i.strip('\n'), 'rb', buffering = 1)
                    if m_office in file.read(5):
                        log_moffice = open('tmp/log_moffice.txt', 'a')
                        log_moffice.write(i)
                        log_moffice.close()
                    file.close()
                except:
                    pass

    tree_txt.close()
    if arg == True:
        result = open('tmp/log_moffice.txt', 'r')
        for a in result:
            dest = '/tmp/moffice/' #Dossier de destination des liens sym pour les JPEG
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier images
                
            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\moffice\\'
                shutil.copy(a.strip('\n'), dest2 + dest3 )


    



