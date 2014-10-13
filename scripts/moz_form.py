import re
from Registry import Registry
import os
import sqlite3
import sys
import time
def moz_form():
    """Cherche la bdd sqlite de mozilla et affiche le domaine des cookies"""
    list_field = []
    field_valeur = []
    tree = open("tmp/log_tree.txt", "r")
    
    for line in tree:
        
        t = re.match(r".*\\Users\\.*\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\.*\\formhistory.sqlite\s", line) #Cherche la base cookies de mozilla
        if t:
            path = str(line)
            conn = sqlite3.connect(path.strip('\n'))
            c = conn.cursor()
            c.execute('select fieldname, value from moz_formhistory')
            
            for row in c:
                list_field.append(row[0])
                field_valeur.append(row[1])
                            
            
                
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





