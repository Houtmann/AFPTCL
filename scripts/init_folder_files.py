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


def make_dir():
    """Create folders needed"""
    path = os.path.abspath('.')
    print(path)
    try:
        os.mkdir(path + '/tmp')
        tmp = path + '/tmp'
        os.mkdir(tmp + '/jpg')
        os.mkdir(tmp + '/gif')
        os.mkdir(tmp + '/docs')
        os.mkdir(tmp + '/videos')
        os.mkdir(tmp + '/pdf')
        os.mkdir(tmp + '/png')
        os.mkdir(tmp + '/moffice')
        os.mkdir(tmp + '/tiff')
    except:
        pass


def create_log():
    """Create files needed"""
    create_css = open(os.path.abspath('.') + '/index.css', 'w')
    create_tree = open(os.path.abspath('.') + '/tmp/log_tree.txt', 'w')
    create_jpg = open(os.path.abspath('.') + '/tmp/log_jpg.txt', 'w')
    create_gif = open(os.path.abspath('.') + '/tmp/log_gif.txt', 'w')
    create_png = open(os.path.abspath('.') + '/tmp/log_png.txt', 'w')
    create_docs = open(os.path.abspath('.') + '/tmp/log_docs.txt', 'w')
    create_docs = open(os.path.abspath('.') + '/tmp/log_pdf.txt', 'w')
    create_docs = open(os.path.abspath('.') + '/tmp/log_videos.txt', 'w')
    create_docs = open(os.path.abspath('.') + '/tmp/log_moffice.txt', 'w')
    create_docs = open(os.path.abspath('.') + '/tmp/log_tiff.txt', 'w')
