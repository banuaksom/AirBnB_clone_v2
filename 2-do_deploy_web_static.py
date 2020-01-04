#!/usr/bin/python3
from os.path import isfile
from fabric.api import *


env.hosts = ['35.196.198.147', '35.229.66.46']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if isfile(archive_path) is False:
        return False
    a_file = archive_path.split('/')[1]
    b_file = a_file.split('.')[0]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(b_file))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(a_file, b_file))
        run("rm /tmp/{}".format(a_file))
        run("mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(b_file, b_file))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(b_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
/data/web_static/current".format(b_file))
        print("New version deployed!")
        return True
    except Exception:
        return False
