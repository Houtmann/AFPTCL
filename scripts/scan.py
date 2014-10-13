# -*- coding: latin1 -*-
import os
import sys
import binascii
import glob

def scan(adress):
    path = os.path.abspath('.')
    list_test = []
    for root, dirs, files in os.walk(adress): #Parcours le disque
        for file in files:
            if file:
                try:        
                    log = open(path + '\\tmp\\log_tree.txt', 'a')      
                    log.write(os.path.join(root, file))
                    log.write("\n")
                    log.close()     
                    lien = os.path.join(root, file)
                except:
                    pass





    


