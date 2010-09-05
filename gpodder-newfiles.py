#!/usr/bin/python2
from time import sleep,strftime
import mpdext

mpd = mpdext.MPDClientExt()
mpd.connect('localhost','6600')

oldfiles = mpd.files_in_dir('Podcasts')

mpd.update('Podcasts')
while 'updating_db' in mpd.status().keys():
    sleep(2)

newfiles = mpd.files_in_dir('Podcasts')
mpd.save_playlist(newfiles.difference(oldfiles),strftime("%Y-%m-%d-%H-%M"))
