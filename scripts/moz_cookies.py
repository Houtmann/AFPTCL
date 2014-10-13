import re
from Registry import Registry
import os
import sqlite3
import sys
import time

def moz_cookies():
    
    """Cherche la bdd sqlite de mozilla et affiche le domaine des cookies"""
    list_cook = []
    cookies_date = []
    cookies_info = {}
    tree = open("tmp/log_tree.txt", "r")
    
    for line in tree:
        t = re.match(r".*\\Users\\.*\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\.*\\cookies.sqlite\s", line) #Cherche la base cookies de mozilla
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

    #print(list_cook)
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
                 
    

