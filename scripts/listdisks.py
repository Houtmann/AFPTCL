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

import psutil
import sys


def list_disk():
    """fonction qui sert à lister les disques présents
    et mounter sur le systéme"""

    list_d = []
    if 'win' in sys.platform:
        t = psutil.disk_partitions(all=False)
        for i in t:
            
            list_d.append(i[0])
        return list_d

    elif 'linux' in sys.platform:
        t = psutil.disk_partitions(all=False)
        for i in t:
            
            list_d.append(i[1])
        return list_d




