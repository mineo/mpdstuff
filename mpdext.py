import mpd

class MPDClientExt(mpd.MPDClient):
    def files_in_dir(self,dir):
        files = set()
        for i in self.listall(dir):
            try:
                files.add(i['file'])
            except KeyError:
                pass
        return files

    def save_playlist(self,playlist,name):
        mpd_playlist_dir = '/home/wieland/.mpd/playlists/'
        with open(mpd_playlist_dir + name + '.m3u','w') as playlist_file:
            for file in playlist:
                print file
                playlist_file.write(file+'\n')
        playlist_file.close()
