import json
import platform

def artistname(user):
    if platform.system() == 'Linux':
        creatorfile='/mnt/b/pl0x/pictures/Gallery-dl/kemonocreators.json'
    else:
        creatorfile='B:\pl0x\Pictures\Gallery-dl\kemonocreators.json'
    with open(creatorfile, encoding='utf-8') as kemonocreator:
        cj=json.load(kemonocreator)
    for creator in cj:
        if user in creator['id']:
            return creator['name']