import os
import sys
import time

def search_videos():
        sign = [b'RIFF',
                b'\x00\x00\x00 ftypisom' ,
                b'\x1aE\xdf\xa3',
                b'FLV.',
                b'ftypM4A',
                b'ftypMSNV',
                b'ftypisom',
                b'ftypmp42',
                b'ftypqt']

        list_file = []
        tree_txt = open('tmp/log_tree.txt', 'r')
        for i in tree_txt.readlines():
            if i:
                try:
                    file = open(i.strip('\n'), 'rb+', buffering=500)
                    for o in sign:
                        if o  in file.read(20):
                            list_file.append(i)
                            log_file = open('tmp/log_videos.txt', 'a')
                            log_file.write(i)
                except:
                    pass
                                                    
        
