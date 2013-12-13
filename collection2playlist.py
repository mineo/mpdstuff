"""Add all tracks in a given MusicBrainz collection to the current playlst.

Usage:
    collection2playlist.py collectionid username password
"""
import musicbrainzngs as m
import sys

from common import connect_to_mpd
from functools import partial

m.set_useragent("collection2playlist", "Mineo")

parse_releaselist = lambda l: map(lambda r: r["id"], l)

parse_collection = lambda c: parse_releaselist(c["release-list"])

def get_releases_in_collection(collectionid):
    releaseids = []
    offset = 0
    found = True

    while found:
        res = m.get_releases_in_collection(collectionid, offset=offset)
        found = len(res["collection"]["release-list"]) > 0
        releaseids += parse_collection(res["collection"])
        offset += 25

    return releaseids

def add_release_to_playlist(mpdclient, releaseid):
    mpdclient.searchadd("musicbrainz_albumid", releaseid)

def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)

    m.auth(sys.argv[2], sys.argv[3])

    mpdclient = connect_to_mpd()
    add_release = partial(add_release_to_playlist, mpdclient)

    map(add_release, get_releases_in_collection(sys.argv[1]))


if __name__ == '__main__':
    main()
