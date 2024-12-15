from typing import Optional
import argparse
import sys
from pathlib import Path

from ...tools.comm.event_pkg import Event
from ...tools.comm.service_pkg import Client

class CLIMain:
    def __init__(self, pls_dir_path: Optional[str] = None):
        """
        CLI için Mizika sınıfını başlatır.
        
        :param pls_dir_path: Playlist dosyalarının bulunduğu dizin
        """
        if pls_dir_path is None:
            pls_dir_path = str(Path.home() / '.muzika' / 'playlists')
        
        # Dizini oluştur
        Path(pls_dir_path).mkdir(parents=True, exist_ok=True)
        
        # Event tanımlamaları
        self.e_play = Event('play')
        self.e_pause = Event('pause')
        self.e_next = Event('next')
        self.e_previous = Event('previous')
        self.e_add_playlist = Event('add_playlist')
        self.e_remove_playlist = Event('remove_playlist')
        self.e_add_song = Event('add_song')
        self.e_remove_song = Event('remove_song')
        
        self.c_play_pl = Client("Play Playlist")
        self.c_edit_pl = Client("Edit Playlist")
        self.c_pl_list = Client("Playlist List")

    def 

def main():
    cli = CLIMain()
    cli.run()

if __name__ == "__main__":
    main()
