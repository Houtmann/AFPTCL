# This file is part of AFPT.

# AFPT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AFPT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AFPT.  If not, see <http://www.gnu.org/licenses/>
# You can read the license.txt in parent directory

import os
import sys
import shutil
import os.path


def search_jpeg(arg):
    jpeg = b'\xFF\xD8'  # Signature du Jpeg
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
        if i:
            try:
                file = open(i.strip('\n'), 'rb', buffering=1)

                if jpeg in file.read(2):
                    log_jpg = open('tmp/log_jpg.txt', 'a')
                    log_jpg.write(i)
                    log_jpg.close()
                file.close()
            except:
                pass

    tree_txt.close()
    if arg:
        result = open('tmp/log_jpg.txt', 'r')
        for a in result:
            dest = '/tmp/jpg/'  # Dossier de destination des liens sym pour les JPEG
            if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'),
                                                           dest))  # Crée des liens symboliques dans le dossier images

            elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\jpg\\'
                shutil.copy(a.strip('\n'), dest2 + dest3)


    



