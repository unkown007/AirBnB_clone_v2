#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack web_static folder into a .tgz file """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    fpath = "versions/web_static_{}.tgz".format(dt)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(fpath)).failed is True:
        return None
    return fpath
