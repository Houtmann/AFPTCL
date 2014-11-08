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

__author__ = 'hadmagic'

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    print('\n'+ fn)
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    #print(TAGS)
    for tag, value in info.items():

        ex = TAGS.get(tag)
        if ex == 'MarkedNote':
            pass
        else:
            print(str(ex) +' : ' + str(value))

    #return ret


