#!/usr/bin/env python2
import logging
import pylast
import sys

from os import getenv
from common import connect_to_mpd, connect_to_lastfm

def main():
    if not len(sys.argv) == 2:
        sys.exit()

    user = sys.argv[1]

    mpd = connect_to_mpd()

    network = connect_to_lastfm()
    user = network.get_user(user)
    tracks = user.get_top_tracks()

    for index, track in enumerate( tracks ):
        item = track.item
        results = mpd.search("musicbrainz_trackid", item.get_mbid())
        if len(results) > 0:
            mpd.add(results[0]["file"])
        else:
            results = mpd.search("artist", item.get_artist(), "title",
                    item.get_title())
            if len(results) > 0:
                mpd.add(results[0]["file"])

if __name__ == '__main__':
    main()
