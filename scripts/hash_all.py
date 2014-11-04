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
import hashlib
import sqlite3


def create_db():
    try:
        open('tmp/files_hash.db', 'r')
    except:
        bdd = open('tmp/files_hash.db', 'w')

        conn = sqlite3.connect('tmp/files_hash.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE files (file text, hash text)''')


def hash_all():
    files = open('tmp/log_tree.txt', 'r')
    hsh = hashlib.md5()
    conn = sqlite3.connect('tmp/files_hash.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE files (file text, hash text)''')

    except:
        pass
    for file in files.readlines():
        read_size = 1024  # You can make this bigger
        try:
            with open(file.strip('\n'), 'rb+') as f:
                for chunk in iter(lambda: f.read(8192), b''):  # for big files test on 120gb filesize
                    hsh.update(chunk)
                hasht = hsh.hexdigest()
                c.execute('''INSERT INTO files (file, hash) VALUES(?, ?)''', [file, hasht])

        except:
            pass

    conn.commit()
    c.close()