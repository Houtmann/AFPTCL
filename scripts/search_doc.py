import ctypes
import os
import sys
import binascii
from tempfile import mkstemp
import glob
import shutil
import os.path

def sumfile(filePath):
	fileObj = open(filePath, 'rb')
	m = hashlib.md5()
	while True:
		d = fileObj.read(50000)
		if not d:
			break
		m.update(d)
	return m.hexdigest()

def search_doc():
     
    doc = b'PK' #Signature du zip, ods...
    list_doc = []
    
    tree_txt = open('tmp/log_tree.txt', 'r')
    for i in tree_txt.readlines():
            if i:
                    try:
                        file = open(i.strip('\n'), 'rb+', buffering=500)
                        if doc in file.read(3):
                            list_doc.append(i)
                            log_doc = open('tmp/log_doc.txt', 'a')
                            log_doc.write(i)
                    except:
                        pass
       
    result = open('tmp/log_doc.txt', 'r')

    for a in result:
        dest = '/tmp/doc/' #Dossier de destination des liens sym pour les docs
        if 'linux' in sys.platform:
                os.system(""" ln -s "{0}" "{1}" """.format(a.strip('\n'), dest )) #Crée des liens symboliques dans le dossier 
                
        elif 'win' in sys.platform:
                tempath = os.path.abspath('.')
                dest2 = tempath.strip('scripts')
                dest3 = '\\tmp\\docs\\'
                shutil.copy(a.strip('\n'), dest2 + dest3 )





