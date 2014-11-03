# -*- coding: latin1 -*-
import os
import sys
import glob

def scan(adress):
    path = os.path.abspath('.')
    list_test = []
    for root, dirs, files in os.walk(adress): #Parcours le disque
        for file in files:
            if file:
                try:        
                    log = open(path + '\\tmp\\log_tree.txt', 'a')
                    list_test.append(os.path.join(root, file))
                    sys.stdout.write("\rNombre de fichiers trouvés: {0}".format(len(list_test)))
                    log.write(os.path.join(root, file))
                    log.write("\n")
                    log.close()     
                    lien = os.path.join(root, file)
                except:
                    pass





    


