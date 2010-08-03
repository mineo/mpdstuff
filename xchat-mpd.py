__module_name__ ="MPD announcer"
__module_version__ = "0.1"
__module_decription__ = "Well, displays MPD info in a channel. \
        Customizable by editing the script"
__module_author__ = "Wieland Hoffmann <themineo@gmail.com>"

import xchat
from os import getenv

""" Set up the basic stuff """
try:
    import mpd
except:
    xchat.prnt("Couldn't load the mpd module")

mpd_host = getenv("MPD_HOST","localhost")
mpd_port = getenv("MPD_PORT","6600")
""" put your password here """
mpd_pass = None

client = mpd.MPDClient()
client.connect(mpd_host,mpd_port)
if mpd_pass:
    client.password(mpd_pass)

def announce_cb(word, word_eol, userdata):
	global client
	client.connect("localhost","6600")
	channel = xchat.get_info("channel")
	try:
		song = client.currentsong()
	except mpd.ConnectionError,e:
		xchat.prnt("Connection error %s" % e)
		return xchat.EAT_ALL
	album = song["album"]
	""" Well, now follows the part which you have to customize for \
		a different output """
	title = song["title"]
	artist = song["artist"]
	xchat.command("msg %s np: %s - %s [%s]" \
		% (channel, artist, title, album))
	return xchat.EAT_ALL


xchat.hook_command("np",announce_cb)
