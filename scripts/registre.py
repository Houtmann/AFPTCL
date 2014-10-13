from Registry import Registry
import os
import sqlite3
import re
import sys

eldem = "Elements de démarrage du systeme : \n\n"
elusb = "Clés USB et Derniere utilisation : \n\n"

def user(adress):
    
    registry = Registry.Registry(adress + "/Windows/System32/config/SOFTWARE")
    users_paths_list = []
    
    k = registry.open("Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\") 
    for v in k.values():
        if v.name() == "ProfileImagePath":
            users_paths_list.append(v.value())
    print (users_paths_list)
    

def boot(adress):
    
    file = []      
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SOFTWARE" )
    key = registry.open("""Microsoft\\Windows\\CurrentVersion\\Run\\""")    
    for v in key.values():
            file.append(v.value()+ "\n")
            print(v.value())
    return file

def boot_2(adress):
    file = []      
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SOFTWARE" )
    key = registry.open("""Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run\\""")    
    for v in key.values():
            file.append(v.value()+ "\n")
            print(v.value())
    return file
           
def usb_1(adress):    #Clé usb et date de derniere utilisatation :
    file_usb = {}
    registry = Registry.Registry(adress.strip("""\\""") + "/Windows/System32/config/SYSTEM")
    key = registry.open("""ControlSet001\\Enum\\USBSTOR""")
    
    for v in key.subkeys():
        for i in v.subkeys():
            for o in i.values():
                if o.name() == "FriendlyName":
                    file_usb [o.value()] = str(i.timestamp())
    
    return file_usb

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


    
    

    





