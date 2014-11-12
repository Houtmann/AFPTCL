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

import re
import sqlite3
import os.path
import shutil


def moz_form():
    """Cherche la bdd sqlite de mozilla et affiche le domaine des cookies"""
    list_field = []
    field_valeur = []
    tree = open("tmp/log_tree.txt", "r")

    for line in tree:

        t = re.match(r".*Users\\.*\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\.*\\formhistory.sqlite\s",
                     line)  # Cherche la base cookies de mozilla
        if t:
            path = str(line)
            tempath = os.path.abspath('.')
            
            shutil.copy(path.strip('\n'), tempath + '/tmp/mozdb/')
            

            conn = sqlite3.connect(tempath + '/tmp/mozdb/formhistory.sqlite')
            c = conn.cursor()
            c.execute('select fieldname, value from moz_formhistory')

            for row in c:
                list_field.append(row[0])
                field_valeur.append(row[1])
        else:
            pass

    report = open('moz_forms.html', 'a')

    report.write('''<html>
        <head>
	<title>Firefox Forms</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <div id="header">Firefox Forms</div>
        <div id="content">
        <table>
        <thead>
	<tr>
		<th>URL</th>
		<th>Date/Time</th>
		
	</tr>
</thead>
	''')
    i = 0
    while i < len(list_field):
        report.write('''<tr><td>{0}</td> <td>{1}</td></tr>'''.format(list_field[i], field_valeur[i]))
        i += 1

    report.write('''</table></div></body></html>''')





