'''
MCore, temel çalma işlevlerinin kolay bir erişim ile sunulduğu bir sınıftır.
MCore sınıfı, "mizika" paketinin çekirdeğidir.

MCore sınıfı müzik çalma işlevi için python-vlc kullanır.
'''
import vlc
import time
from typing import Optional
from ...tools.comm.event_pkg import Event
from .song import Song
from .consts import *

class MCore:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        
        self.state: bool = False  # is playing or paused
        self.volume: float = 50.0  # default volume at 50%
        self.position: float = 0.0  # how much spending time for playing music
        self.curr_song: Optional[Song] = None  # current playing song
        self.__run_flag: bool = False  # is running 
        #
        # Events
        #
        self.e_state = Event("state changed")
        self.e_vol = Event("volume changed")
        self.e_curr_song = Event("song changed")

    def load_song(self, song: Song):
        '''Şarkıyı oynatıcıya yükler'''
        media = self.instance.media_new(song.path)
        self.player.set_media(media)
        self.curr_song = song
        self.e_curr_song.trigger()

    #
    # State
    #

    def state_togg(self):
        '''çalma durumunu için bir toggle'''
        if self.state: self.pause()
        else: self.play()

    def play(self):
        '''
        "state"i true olarak ayarlar. Müziği başlatır veya
        devam ettirir. Zaten çalıyorsa birşeye ellemez
        '''
        if not self.state and self.curr_song:
            self.player.play()
            self.state = True
            self.e_state.trigger()

    def pause(self):
        '''Müzik çalmayı duraklatır'''
        if self.state:
            self.player.pause()
            self.state = False
            self.e_state.trigger()

    #
    # Position
    #

    def get_pos(self):
        return self.player.get_time() / S_TO_MS

    def set_pos(self, new_pos: float):
        '''Şarkının pozisyonunu "new_pos" olarak ayarlar'''
        if self.curr_song:
            self.player.set_time(new_pos * S_TO_MS)

    def rewind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar geriye sarar'''
        self.set_pos(
            max(0.0, self.position - val)
        )

    def towind(self, val: float = DEFAULT_WIND):
        '''Şarkının pozisyonunu "val" kadar ileriye sarar'''
        self.set_pos(
            min(
                self.curr_song.length,
                self.position + val
            )
        )

    #
    # Volume
    #

    def set_vol(self, percent: float):
        '''
        Ses düzeyini "percent" olarak ayarlar
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arasına getirilir
        '''
        if percent < 0: percent = 0
        elif percent > 100: percent = 100
        
        self.player.audio_set_volume(int(percent))
        self.volume = percent
        self.e_vol.trigger()

    def mute(self):
        '''Ses düzeyini 0.0'a eşitler'''
        self.set_vol(0.0)

    def inc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar artırır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        self.set_vol(self.volume + percent)

    def desc_vol(self, percent: float):
        '''
        Ses düzeyini "percent" kadar azaltır
        Dikkat edilmesi gereken husus "percent" 0 ila 100 arası olmalıdır
        '''
        self.set_vol(self.volume - percent)

    #
    # Threading
    #

    def spin(self):
        '''
        Eğer müzik çalmak için ayrı bir threadin üstüne düşmesi
        isteniyorsa bu method çalıştırılmalı
        '''
        while self.__run_flag:
            if self.curr_song == None:
                self.position = self.get_pos()
            time.sleep(ZZZ_TIME)            
        
