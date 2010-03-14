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
client.connect("localhost",6600)

def announce_cb(word, word_eol, userdata):
	global client
	channel = xchat.get_info("channel")
	try:
		song = client.currentsong()
	except mpd.ConnectionError,e:
		xchat.prnt("Connection error"+e)
		return xchat.EAT_ALL
	album = song["album"]
	""" Well, now follows the part which you have to customize for \
		a different output """
	title = song["title"]
	artist = song["artist"]
	xchat.command("msg %s np: %s - %s [%s]" \
		% (channel,artist,title,album))
	return xchat.EAT_ALL

def unload_cb(userdata):
	global client
	client.disconnect()


xchat.hook_unload(unload_cb)
xchat.hook_command("np",announce_cb)
