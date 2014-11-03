import os
import sys
import glob
import shutil
import os.path


def search_tiff(arg):
    tiff = b'II'  # Signature du tiff
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
        if i:
            try:
                file = open(i.strip('\n'), 'rb', buffering=1)

                if tiff in file.read(2):
                    log_tiff = open('tmp/log_tiff.txt', 'a')
                    log_tiff.write(i)
                    log_tiff.close()
                file.close()
            except:
                pass

    tree_txt.close()
    if arg:
        result = open('tmp/log_tiff.txt', 'r')
        for a in result:
            dest = '/tmp/tiff/'  # Dossier de destination des liens sym
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'),
                                                           dest))  # Crée des liens symboliques dans le dossier images

            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\tiff\\'
                shutil.copy(a.strip('\n'), dest2 + dest3)


    



