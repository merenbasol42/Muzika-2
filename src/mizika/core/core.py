'''
MCore, temel çalma işlevlerinin kolay bir erişim ile sunulduğu bir sınıftır.
MCore sınıfı, "mizika" paketinin çekirdeğidir.

MCore sınıfı müzik çalma işlevi için python-vlc kullanır.
'''
import vlc
from .song import Song
from .consts import DEFAULT_WIND
from typing import Optional

class MCore:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        
        self.state: bool = False  # is playing or paused
        self.volume: float = 50.0  # default volume at 50%
        self.position: float = 0.0  # how much spending time for playing music
        self.curr_song: Optional[Song] = None  # current playing song
        self.__run_flag: bool = False  # is running 

    def load_song(self, song: Song):
        '''Şarkıyı oynatıcıya yükler'''
        media = self.instance.media_new(song.path)
        self.player.set_media(media)
        self.curr_song = song
        self.player.audio_set_volume(int(self.volume))

    #
    # State
    #

    def state_togg(self):
        '''çalma durumunu için bir toggle'''
        if self.state:
            self.pause()
        else:
            self.play()

    def play(self):
        '''
        "state"i true olarak ayarlar. Müziği başlatır veya
        devam ettirir. Zaten çalıyorsa birşeye ellemez
        '''
        if not self.state and self.curr_song:
            self.player.play()
            self.state = True

    def pause(self):
        '''Müzik çalmayı duraklatır'''
        if self.state:
            self.player.pause()
            self.state = False

    #
    # Position
    #
    
    def set_pos(self, new_pos: float):
        '''Şarkının pozisyonunu "new_pos" olarak ayarlar'''
        if self.curr_song:
            total_length = self.player.get_media().get_duration()
            self.player.set_time(int(total_length * new_pos))

    def rewind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar geriye sarar'''
        current_time = self.player.get_time()
        total_length = self.player.get_media().get_duration()
        new_time = max(0, current_time - int(total_length * val))
        self.player.set_time(new_time)

    def towind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar ileriye sarar'''
        current_time = self.player.get_time()
        total_length = self.player.get_media().get_duration()
        new_time = min(total_length, current_time + int(total_length * val))
        self.player.set_time(new_time)

    #
    # Volume
    #

    def set_vol(self, percent: float):
        '''
        Ses düzeyini "percent" olarak ayarlar
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        if 0 <= percent <= 100:
            self.volume = percent
            self.player.audio_set_volume(int(percent))

    def mute(self):
        '''Ses düzeyini 0.0'a eşitler'''
        self.set_vol(0.0)

    def inc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar artırır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        if 0 <= percent <= 100:
            new_volume = min(100, self.volume + percent)
            self.set_vol(new_volume)

    def desc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar azaltır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        if 0 <= percent <= 100:
            new_volume = max(0, self.volume - percent)
            self.set_vol(new_volume)

    #
    # Threading
    #

    def spin(self):
        '''
        Eğer müzik çalmak için ayrı bir threadin üstüne düşmesi
        isteniyorsa bu method çalıştırılmalı
        '''
        # Bu metod, gelecekte thread bazlı müzik çalma için kullanılabilir
        # Şimdilik boş bırakılmıştır
        pass
