#!/usr/bin/python
import mpd
from time import sleep

def files_in_dir(mpd,dir):
    files = set()
    for i in mpd.listall(dir):
        try:
            files.add(i[file])
        except KeyError:
            pass
    return files

mpd = mpd.MPDClient()
mpd.connect('localhost','6600')

oldfiles = files_in_dir(mpd,'Podcasts')

mpd.update('Podcasts')
mpd.clear()
if 'updating_db' in mpd.status().keys():
    sleep(2)

newfiles = files_in_dir(mpd,'Podcasts')

for file in newfiles.difference(oldfiles):
    mpd.add(file)
