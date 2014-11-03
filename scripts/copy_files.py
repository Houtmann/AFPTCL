import shutil
import os.path
import sys



def copy_files():
    t = os.path.abspath('.')
    log_video = open('log_videos.txt', 'r')
    for i in log_video:
        dest = '/tmp/videos'  # Dossier de destination des liens sym
        if 'linux' in sys.platform:
            os.system(
                """ ln -s "{0}" "{1}" """.format(i.strip('\n'), dest))  # Crée des liens symboliques dans le dossier

        elif 'win' in sys.platform:
            tempath = os.path.abspath('.')
            dest2 = tempath.strip('scripts')
            dest3 = '\\tmp\\videos\\'
            shutil.copy(i.strip('\n'), dest2 + dest3)
