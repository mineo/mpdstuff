#!/usr/bin/env python
# Allows to load lastfm:// playlists in mpd 
# for usage just check the optionParser options
# 
# Feel free to redistribute

from optparse import OptionParser
import mpd
mpd = mpd.MPDClient()

def add_to_mpd(type,station):
    if station:
        for i in station[0].split(','):
            if type in ['artist','user','globaltags']:
                print 'adding lastfm://'+type+'/'+i.replace(' ','+')
                mpd.load('lastfm://'+type+'/'+i.replace(' ','+'))
            else:
                print 'adding lastfm://user/'+i+'/recommendations'
                mpd.load('lastfm://user/'+i+'/recommendations')

if __name__ == "__main__":
    opts = OptionParser()
    opts.add_option("-a","--artist",action="append")
    opts.add_option("-u","--user",action="append")
    opts.add_option("-t","--globaltags",action="append")
    opts.add_option("-r","--recommendations",action="append")
    (options, args) = opts.parse_args()

    mpd.connect('localhost','6600')

    for values in vars(options).iteritems():
            add_to_mpd(values[0],values[1])
