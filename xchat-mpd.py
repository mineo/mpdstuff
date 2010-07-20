__module_name__ ="MPD announcer"
__module_version__ = "0.1"
__module_decription__ = "Well, displays MPD info in a channel. \
		Customizable by editing the script"

import xchat
try:
	import mpd
except:
	xchat.prnt("Couldn't load the mpd module")
client = mpd.MPDClient()
def announce_cb(word, word_eol, userdata):
	global client
	client.connect("localhost","6600")
	channel = xchat.get_info("channel")
	try:
		song = client.currentsong()
	except mpd.ConnectionError,e:
		xchat.prnt("Connection error"+e)
	else:
		album = song["album"]
		title = song["title"]
		artist = song["artist"]
		xchat.command("msg %s np: %s - %s [%s]" \
			% (channel,artist,title,album))
		client.disconnect()
	return xchat.EAT_ALL


xchat.hook_command("np",announce_cb)
