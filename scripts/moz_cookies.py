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
import time


def moz_cookies():
    """Cherche la bdd sqlite de mozilla et affiche le domaine des cookies"""
    list_cook = []
    cookies_date = []
    cookies_info = {}
    tree = open("tmp/log_tree.txt", "r")

    for line in tree:
        t = re.match(r".*\\Users\\.*\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\.*\\cookies.sqlite\s",
                     line)  # Cherche la base cookies de mozilla
        if t:
            path = str(line)

            conn = sqlite3.connect(path.strip('\n'))
            c = conn.cursor()
            c.execute('select baseDomain, lastAccessed/1000000 from moz_cookies')
            for row in c:
                nombre = row[1]
                date = time.ctime(row[1])

                list_cook.append(row[0])
                cookies_date.append(date)
                cookies_info[row[0]] = date

    # print(list_cook)
    report = open('moz_cookies.html', 'a')

    report.write('''<html>
        <head>
	<title>Web Cookies</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <div id="header">Firefox cookies</div>
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
    while i < len(list_cook):
        report.write('''<tr><td>{0}</td> <td>{1}</td></tr>'''.format(list_cook[i], cookies_date[i]))
        i += 1

    report.write('''</table></div></body></html>''')
                 
    

