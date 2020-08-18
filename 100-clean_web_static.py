#!/usr/bin/python3
""" Fabric script that distributes an archive to a web server. """
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists
env.hosts = ["35.237.133.118", "3.90.191.97"]

def do_clean(number=0):
    """ Delete out-of-date files. """
    n = int(number)
    with lcd("versions"):
        if n == 0 or n == 1:
            local("ls -t | tail -n +2 | xargs rm -rfv")
        else:
            local("ls -t | tail -n + {} | xargs rm -rfv".format(n + 1))

    with cd("/data/web_static/releases/"):
        if n == 0 or n == 1:
            run("ls -t | tail -n +2 | xargs rm -rfv")
        else:
            run("ls -t | tail -n {} | xargs rm -rfv".format(n + 1))
