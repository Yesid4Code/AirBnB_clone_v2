#!/usr/bin/python3
""" Fabric script that distributes an archive to a web server. """
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists
env.hosts = ["35.237.133.118", "3.90.191.97"]


def do_pack():
    """ Collect files from the web_static folder. """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    capture = local("tar -cvzf {} web_static".format(file_name))
    if capture.succeeded:
        return file_name
    return None


def do_deploy(archive_path):
    """ Deploy an archive to the web server. """
    if exists(archive_path) is False:
        return False
    try:
        file_tgz = archive_path.split("/")[1]  # filename.tgz
        file_name = file_tgz.split(".")[0]  # filename
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, file_name))
        # Uncompress the archive to the folder.
        run("tar -xzf /tmp/{} -C {}{}/".format(file_tgz, path, file_name))
        # Deletes the collected file
        run("rm /tmp/{}".format(file_tgz))
        run("mv {0}{1}/web_static/* {0}{1}".format(path, file_name))
        run("rm -rf {}{}/web_static".format(path, file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, file_name))

        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to the web servers. """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
