#!/usr/bin/python3
from datetime import datetime
from os.path import isfile
from fabric.api import *

def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    local("tar cvzf versions/web_static_{}.tgz web_static".format(cur_time))
    if isfile("versions/web_static_{}.tgz".format(cur_time)):
        return "versions/web_static_{}.tgz".format(cur_time)
