import os
import sys


def make_log():
    
    report = open('Report.html', 'a')
    report.write('''<html>
        <head>
	<title>Report</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <div id="header">Report</div>
        <div id="content">
        <table>
        <thead>
	<tr>
		<th>URL</th>
		<th>Date/Time</th>
		
	</tr>
</thead>''')


    log_tree = []
    for i in open('tmp/log_tree.txt', 'r').readlines():
        log_tree.append(i)
    report.write('''<tr><td>Nombres de fichiers :</td> <td>{0}</td></tr>'''.format(len(log_tree)))

    log_jpg = []
    for i in open('tmp/log_jpg.txt', 'r').readlines():
        log_jpg.append(i)
    report.write('''<tr><td>Nombres de JPG :</td> <td>{0}</td></tr>'''.format(len(log_jpg)))

    log_gif = []
    for i in open('tmp/log_gif.txt', 'r').readlines():
        log_gif.append(i)
    report.write('''<tr><td>Nombres de GIF :</td> <td>{0}</td></tr>'''.format(len(log_gif)))

    log_png = []
    for i in open('tmp/log_png.txt', 'r').readlines():
        log_png.append(i)
    report.write('''<tr><td>Nombres de PNG :</td> <td>{0}</td></tr>'''.format(len(log_png)))

    log_doc = []
    for i in open('tmp/log_docs.txt', 'r').readlines():
        log_doc.append(i)
    report.write('''<tr><td>Nombres de Documents :</td> <td>{0}</td></tr>'''.format(len(log_doc)))

    log_videos = []
    for i in open('tmp/log_videos.txt', 'r').readlines():
        log_videos.append(i)
    report.write('''<tr><td>Nombres de Videos :</td> <td>{0}</td></tr>'''.format(len(log_videos)))

    report.write('''</table></div></body></html>''')

        
    
