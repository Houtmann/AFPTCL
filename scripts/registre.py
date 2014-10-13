from Registry import Registry
import os
import sqlite3
import re
import sys


def user(adress):
    
    registry = Registry.Registry(adress + "/Windows/System32/config/SOFTWARE")
    users_paths_list = []
    
    k = registry.open("Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\") 
    for v in k.values():
        if v.name() == "ProfileImagePath":
            users_paths_list.append(v.value())
    print (users_paths_list)
    

def boot(adress):
    report = open('registre.html', 'a')
    report.write('''<html>
        <head>
	<title>Registre Windows</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <div id="header">Registre windows</div>
        <div id="content">
        <table>
        <thead>
	<tr>
		<th>Software On Boot</th>
		
		
	</tr>
</thead>
	''')
    
    file = []      
    registry = Registry.Registry(adress + "Windows/System32/config/SOFTWARE" )
    key = registry.open("""Microsoft\\Windows\\CurrentVersion\\Run\\""")
    
    for v in key.values():
            file.append(v.value()+ "\n")
            report.write('<tr><td>{0}'.format(v.value()))
    
    return file


def boot_2(adress):
    report = open('registre.html', 'a')
    file = []      
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SOFTWARE" )
    key = registry.open("""Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run\\""")
    
    for v in key.values():
            report.write('<tr><td>{0}</tr>'.format(v.value())) 
    return file

           
def usb_1(adress):    #Clé usb et date de derniere utilisatation :
    report = open('registre.html', 'a')
    report.write('''
        <table>
        <thead>
	<tr>
	<th>USB DEVICES :</th>
	<th>DATE / TIME :</th>
	</tr>
        </thead>''')
    
    file_usb = {}
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SYSTEM")
    key = registry.open("""ControlSet001\\Enum\\USBSTOR""")
    
    for v in key.subkeys():
        for i in v.subkeys():
            for o in i.values():
                if o.name() == "FriendlyName":
                    
                    report.write('<tr><td>{0}</td> <td>{1}</td></tr>'.format(o.value(), str(i.timestamp())))
                    
    report.write('''</table></div></body></html>''')

    
    

def usb_2(adress):    #Clé usb et date de derniere utilisatation :
    file_usb = {}
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SYSTEM")
    
    key = registry.open("""ControlSet001\\Enum\\USBSTOR""")
    
    for v in key.subkeys():
        for i in v.subkeys():
            for o in i.values():
                if o.name() == "FriendlyName":
                    file_usb [o.value()] = str(i.timestamp())
    
    return file_usb


    
    

    





