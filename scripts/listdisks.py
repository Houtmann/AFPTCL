import psutil
import sys


def list_disk():
    """fonction qui sert à lister les disques présents
    et mounter sur le systéme"""

    list_d = []
    if 'win' in sys.platform:
        t = psutil.disk_partitions(all=False)
        for i in t:
            
            list_d.append(i[0])
        return list_d

    elif 'linux' in sys.platform:
        t = psutil.disk_partitions(all=False)
        for i in t:
            
            list_d.append(i[1])
        return list_d




