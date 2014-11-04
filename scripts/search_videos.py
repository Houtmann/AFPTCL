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

def search_videos(arg):
    sign = [b'RIFF',
            b'\x00\x00\x00 ftypisom',
            b'\x1aE\xdf\xa3',
            b'FLV.',
            b'ftypM4A',
            b'ftypMSNV',
            b'ftypisom',
            b'ftypmp42',
            b'ftypqt']

    list_file = []
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
        if i:
            try:
                file = open(i.strip('\n'), 'rb+', buffering=500)
                for o in sign:
                    if o in file.read(20):
                        list_file.append(i)
                        log_file = open('tmp/log_videos.txt', 'a')
                        log_file.write(i)
                        log_file.close()
                    file.close()
            except:
                pass
