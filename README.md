AFPT-CL
======

##A forensic python tools command line 

### Update 11/2014:
New features : -hash for hash all files of the disk in sqlite3 database


Need python < 3.3

- Carves files (magic number) (jpg, gif, pdf, png) and symlink or copy files to the tmp directory
- Extract firefox cookies, and forms
- Extract somes datas to Windows registry (usb devices, software on boot)



Usage : python main.py

- optional arguments:
-  -h, --help            show this help message and exit
-  -p PATH, --path PATH  precise path of disk
-  -cv                   Copy videos files in tmp dir
-  -sf                   Don't search files in disk
- -hash                 Hash all files of the disk and store it in sqlite3 db
-  -exif                 Get exif informations on specified jpeg image
