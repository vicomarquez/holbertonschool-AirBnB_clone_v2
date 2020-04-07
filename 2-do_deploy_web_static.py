#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import local
from datetime import datetime
from os import path


env.hosts = ['34.73.76.135', '18.209.20.255']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    if !(path.exists(archive_path)):
        return False

    # upload archive
    result = put(archive_path, '/tmp/')
    if result.failed:
        return False

    # create target dir
    timestamp = archive_path[-18:-4]
    result = run('sudo mkdir -p /data/web_static/\
                 releases/web_static_{}/'i.format(timestamp))
    if result.failed:
        return False

    # uncompress archive and delete .tgz
    result = run('sudo tar -xzf /tmp/web_static_{}.tgz -C\
                 /data/web_static/releases/web_static_{}/'
                 .format(timestamp, timestamp))
    if result.failed:
        return False

    result = run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))
    if result.failed:
        return False

    # re-establish symbolic link
    result = run('sudo ln -sf /data/web_static/releases/web_static_{}\
        /data/web_static/current'.format(timestamp))
    if result.failed:
        return False
