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

from Registry import Registry


def user(adress):
    report = open('registre.html', 'a')
    report.write('''<html>
        <head>
	<title>Registre Windows</title>
	<link rel="stylesheet" type="text/css" href="index.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <div id="content">
        <table>
        <thead>
	<tr>
		<th>Users : </th>
		
		
	</tr>
    </thead>
	''')
    try:
        registry = Registry.Registry(adress + "/Windows/System32/config/SOFTWARE")
        users_paths_list = []

        k = registry.open("Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\")
        for v in k.values():
            if v.name() == "ProfileImagePath":
                users_paths_list.append(v.value())
                report.write('<tr><td>{0}</tr>'.format(users_paths_list))
    except:
        pass


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
    try:

        file = []
        registry = Registry.Registry(adress + "Windows/System32/config/SOFTWARE")
        key = registry.open("""Microsoft\\Windows\\CurrentVersion\\Run\\""")

        for v in key.values():
            file.append(v.value() + "\n")
            report.write('<tr><td>{0}'.format(v.value()))

        return file
    except:
        pass


def boot_2(adress):
    report = open('registre.html', 'a')
    try:
        file = []
        registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SOFTWARE")
        key = registry.open("""Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run\\""")

        for v in key.values():
            report.write('<tr><td>{0}</tr>'.format(v.value()))
        return file
    except:
        pass


def usb_1(adress):  # Clé usb et date de derniere utilisatation :
    report = open('registre.html', 'a')
    report.write('''
        <table>
        <thead>
	<tr>
	<th>USB DEVICES :</th>
	<th>DATE / TIME :</th>
	</tr>
        </thead>''')
    try:
        file_usb = {}
        registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SYSTEM")
        key = registry.open("""ControlSet001\\Enum\\USBSTOR""")

        for v in key.subkeys():
            for i in v.subkeys():
                for o in i.values():
                    if o.name() == "FriendlyName":
                        report.write('<tr><td>{0}</td> <td>{1}</td></tr>'
                                     .format(o.value(), str(i.timestamp())))
    except:
        pass

        # report.write('''</table></div></body></html>''')


def shutdown_time(adress):
    registry = Registry.Registry(adress + "Windows/System32/config/SYSTEM")
    key = registry.open("""ControlSet001\\Control\\Windows\\""")
    for v in key.values():
        if v.name() == 'ShutdownTime':
            print(v.value())
            date = int.from_bytes(v.value(), byteorder='little')
            print(date)


            # print(v.name())



    
    



    
    

    





