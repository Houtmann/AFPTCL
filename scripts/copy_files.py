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
