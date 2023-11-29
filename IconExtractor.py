#penis for bob 8=D
from zipfile import ZipFile
import os
import shutil

def GetmodIcons(modfp):
    micons = {}
    for root, dirs, files in os.walk(modfp, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            key = path
            if name.endswith('.zip'):
                with ZipFile(path) as myzip:
                    infolist = myzip.infolist()
                micons[key] = infolist
    return micons

def GetBaseIcons(basefp):
    bicons = {}
    for root, dirs, files in os.walk(basefp, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            key = name
            bicons[key] = path
    return bicons


if __name__ == "__main__":
    target = "/lifesupport-canister.png"
    modfp= r"C:\Users\rudyb\AppData\Roaming\Factorio\mods"
    basefp = r"C:\Program Files (x86)\Steam\steamapps\common\Factorio\data\base\graphics\icons"
    bicons =GetBaseIcons(basefp)
    for item in bicons:
        print (bicons[item])
    

    
