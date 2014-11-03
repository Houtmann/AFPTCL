import os
import sys
import shutil
import os.path


def search_moffice(arg):
    moffice = b'PK\x03\x04\x14'  # Signature
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
        if i:
            try:
                file = open(i.strip('\n'), 'rb', buffering=1)
                if moffice in file.read(10):
                    log_jpg = open('tmp/log_moffice.txt', 'a')
                    log_jpg.write(i)
                    log_jpg.close()
                    file.close()
            except:
                pass

    tree_txt.close()
    if arg:
        result = open('tmp/log_moffice.txt', 'r')
        for a in result:
            dest = '/tmp/moffice/'  # Dossier de destination des liens sym pour les JPEG
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'),
                                                           dest))  # Crée des liens symboliques dans le dossier images

            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\moffice\\'
                shutil.copy(a.strip('\n'), dest2 + dest3)


    



