#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
from os import path, makedirs, listdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack web_static folder into a .tgz file """
    if not path.isdir("./versions"):
        makedirs("./versions")
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    fpath = "versions/web_static_{}.tgz".format(dt)
    file_tar = local("tar -cvzf {} web_static".format(fpath))
    files = listdir("./versions")
    paths = [path.join("./versions", base_name) for base_name in files]
    if len(paths) == 0:
        return None
    return max(paths, key=path.getctime)
