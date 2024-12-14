from typing import Optional
import argparse
import sys
from pathlib import Path

from ...tools.event_pkg import Event

class MuzikaCLI:
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
        
    
    def run(self):
        """
        CLI için argüman ayrıştırıcı ve çalıştırma metodu.
        """
        parser = argparse.ArgumentParser(description="Muzika CLI")
        
        parser.add_argument('action', choices=[
            'play', 'pause', 'next', 'previous', 
            'add-playlist', 'remove-playlist', 'list-playlists',
            'add-song', 'remove-song', 'list-songs'
        ])
        parser.add_argument('--name', help="Playlist veya şarkı adı")
        parser.add_argument('--song', help="Şarkı dosya yolu")
        
        args = parser.parse_args()
        
        try:
            if args.action == 'play':
                self.e_play.trigger()
                print("Müzik çalıyor.")
            elif args.action == 'pause':
                self.e_pause.trigger()
                print("Müzik duraklatıldı.")
            elif args.action == 'next':
                self.e_next.trigger()
                print("Sonraki şarkıya geçildi.")
            elif args.action == 'previous':
                self.e_previous.trigger()
                print("Önceki şarkıya geçildi.")
            elif args.action == 'add-playlist':
                if args.name:
                    self.e_add_playlist.trigger(args.name)
                    print(f"'{args.name}' playlist'i oluşturuldu.")
                else:
                    print("Playlist adı belirtilmedi.")
            elif args.action == 'remove-playlist':
                if args.name:
                    self.e_remove_playlist.trigger(args.name)
                    print(f"'{args.name}' playlist'i silindi.")
                else:
                    print("Playlist adı belirtilmedi.")
            elif args.action == 'list-playlists':
                playlists = self.mizika.get_playlists()
                if playlists:
                    print("Mevcut Playlistler:")
                    for pl in playlists:
                        print(f"- {pl.name}")
                else:
                    print("Henüz playlist oluşturulmamış.")
            elif args.action == 'add-song':
                if args.name and args.song:
                    self.e_add_song.trigger(args.name, args.song)
                    print(f"Şarkı '{args.song}' '{args.name}' playlist'ine eklendi.")
                else:
                    print("Playlist adı veya şarkı dosya yolu eksik.")
            elif args.action == 'remove-song':
                if args.name and args.song:
                    self.e_remove_song.trigger(args.name, args.song)
                    print(f"Şarkı '{args.song}' '{args.name}' playlist'inden silindi.")
                else:
                    print("Playlist adı veya şarkı dosya yolu eksik.")
            elif args.action == 'list-songs':
                if args.name:
                    songs: list[str] = self.mizika.list_songs_in_playlist(args.name)
                    if songs:
                        print(f"'{args.name}' Playlist'indeki Şarkılar:")
                        for song in songs:
                            print(f"- {song}")
                    else:
                        print(f"'{args.name}' playlist'inde şarkı bulunmuyor.")
                else:
                    print("Playlist adı belirtilmedi.")
        
        except Exception as e:
            print(f"Hata: {e}")
            sys.exit(1)

def main():
    cli = MuzikaCLI()
    cli.run()

if __name__ == "__main__":
    main()
