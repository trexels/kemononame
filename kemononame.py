import json
import platform

def artistname(user):
    if platform.system() == 'Linux':
        creatorfile='~/kemonocreators.json'
    else:
        creatorfile='%userprofile%\kemonocreators.json'
    with open(creatorfile, encoding='utf-8') as kemonocreator:
        cj=json.load(kemonocreator)
    for creator in cj:
        if user in creator['id']:
            return creator['name']
