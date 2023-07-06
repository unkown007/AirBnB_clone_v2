#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack web_static folder into a .tgz file """
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        fpath = "versions/web_static_{}.tgz".format(dt)
        if not os.path.exists("versions"):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(fpath))
        return fpath
    except Exception:
        return None
