#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack web_static folder into a .tgz file """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(dt)
    if not os.path.exists("versions"):
        local("mkdir versions")
    file_tar = local("tar -cvzf {} web_static".format(path))
    if file_tar.succeeded:
        return path
