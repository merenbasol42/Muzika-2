from typing import Optional
import argparse
import sys
from pathlib import Path

from src.mizika.mizika import Mizika

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
        
        self.mizika = Mizika(pls_dir_path)
    
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
                self.mizika.play()
                print("Müzik çalıyor.")
            elif args.action == 'pause':
                self.mizika.pause()
                print("Müzik duraklatıldı.")
            elif args.action == 'next':
                self.mizika.forward()
                print("Sonraki şarkıya geçildi.")
            elif args.action == 'previous':
                self.mizika.backward()
                print("Önceki şarkıya geçildi.")
            elif args.action == 'add-playlist':
                if args.name:
                    self.mizika.create_playlist(args.name)
                    print(f"'{args.name}' playlist'i oluşturuldu.")
                else:
                    print("Playlist adı belirtilmedi.")
            elif args.action == 'remove-playlist':
                if args.name:
                    self.mizika.remove_playlist(args.name)
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
                    self.mizika.add_song_to_playlist(args.name, args.song)
                    print(f"Şarkı '{args.song}' '{args.name}' playlist'ine eklendi.")
                else:
                    print("Playlist adı veya şarkı dosya yolu eksik.")
            elif args.action == 'remove-song':
                if args.name and args.song:
                    self.mizika.remove_song_from_playlist(args.name, args.song)
                    print(f"Şarkı '{args.song}' '{args.name}' playlist'inden silindi.")
                else:
                    print("Playlist adı veya şarkı dosya yolu eksik.")
            elif args.action == 'list-songs':
                if args.name:
                    songs = self.mizika.list_songs_in_playlist(args.name)
                    if songs:
                        print(f"'{args.name}' Playlist'indeki Şarkılar:")
                        for song in songs:
                            print(f"- {song.path}")
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
