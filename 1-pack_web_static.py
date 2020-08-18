#!/usr/bin/python3
""" script that generates a tgz archive. """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Collect files from the web_static folder. """
    time = datetime.now().strftime(%Y%m%d%H%M%S)
    file_name = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    capture = local("tar -cvzf {} web_static".format(file_name))
    if capture.succeeded:
        return file_name
    return None
