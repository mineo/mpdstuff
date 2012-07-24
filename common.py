import mpd
import pylast
from os import getenv
from os.path import join

def connect_to_mpd():
    """Connects to an MPD server via MPD_HOST and MPD_PORT environment
    variables
    :returns: a connected :class:`mpd.MPDClient`

    """
    client = mpd.MPDClient()
    password = None
    host = getenv("MPD_HOST", "localhost")
    if "@" in host:
        password, host = host.split("@")
    port = getenv("MPD_POT", 6600)

    client.connect(host, port)
    if password is not None:
        client.password(password)

    return client

def connect_to_lastfm():
    CONF_FILE = join(getenv("XDG_CONFIG_HOME"),"mpdt","config")
    conf = {}
    with open(CONF_FILE,"r") as configfile:
        for i in configfile.readlines():
            i = i.split(" ")
            conf[i[0]] = i[1][:-1]
    network = pylast.get_lastfm_network(api_key = conf["api_key"],
        api_secret = conf["api_secret"], username = conf["username"],
        password_hash = conf["password"])
    return network
