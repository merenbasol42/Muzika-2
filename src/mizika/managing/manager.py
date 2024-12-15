
'''
MManager (Mizika Manager); "mizika" paketi için oynatma listesi işlemleri
işlevlerini yerine getiren sınıftır.
'''

from typing import Optional, Union
from ...tools.comm.event_pkg import Event
from ..core.core import Song
from .playlist import Playlist
from .pl_list import PLList
from .enums import *

class MManager: #Mizika Manager
    def __init__(self, pls_dir_path: str):
        self.play_mode: str = PLAY_MODE.DEFAULT
        self.index: Optional[int] = None
        self.curr_song: Optional[Song] = None
        self.play_pl: Optional[Playlist] = None
        self.edit_pl: Optional[Playlist] = None
        self.pl_list: PLList = PLList(pls_dir_path)
        #
        # Events
        #
        self.e_play_mode: Event = Event("play_mode_changed") # Play mode has been changed
        self.e_curr_song: Event = Event("curr_song_changed") # Current song has been changed
        self.e_play_pl: Event = Event("edit_pl_changed") # Playing playlist has been changed
        self.e_edit_pl: Event = Event("edit_pl_changed") # Editing playlist has been changed
        self.e_pl_list: Event = Event("pl_list_changed") # PLList's content ch

    def set_play_pl(self, path: str):
        '''Set the playing playlist'''
        try:
            self.play_pl = Playlist(path)
            self.index = 0 if self.play_pl.path_list else None
            self.curr_song = self.play_pl.load_a_song(self.index) if self.index is not None else None
            self.e_play_pl.trigger()
        except Exception as e:
            print(f"Error setting play playlist: {e}")

    def set_play_mode(self, new_mode: str):
        '''Set the play mode'''
        if new_mode in PLAY_MODE.ARR:
            self.play_mode = new_mode
            self.e_play_mode.trigger()
        else:
            raise ValueError(f"Invalid play mode: {new_mode}")

    def play_mode_togg(self):
        '''Toggle play mode in a cyclic manner'''
        current_index = PLAY_MODE.ARR.index(self.play_mode)
        next_index = (current_index + 1) % len(PLAY_MODE.ARR)
        self.play_mode = PLAY_MODE.ARR[next_index]
        self.e_play_mode.trigger()

    def load_song(self, index: int) -> Song:
        '''Load a song at a specific index in the current playlist'''
        if self.play_pl is None:
            raise ValueError("No playlist is currently loaded")
        
        if 0 <= index < len(self.play_pl.path_list):
            self.index = index
            self.curr_song = self.play_pl.load_a_song(index)
            self.e_curr_song.trigger()
            return self.curr_song
        
        raise IndexError("Song index out of range")

    def forward(self) -> Song:
        '''Move to the next song based on play mode'''
        if self.play_pl is None or not self.play_pl.path_list:
            raise ValueError("No playlist or songs available")
        
        if self.play_mode == PLAY_MODE.ONE:
            return self.curr_song if self.curr_song else self.load_song(0)
        
        if self.play_mode == PLAY_MODE.MIX:
            import random
            self.index = random.randint(0, len(self.play_pl.path_list) - 1)
        else:
            self.index = (self.index + 1) % len(self.play_pl.path_list)
        
        return self.load_song(self.index)

    def backward(self) -> Song:
        '''Move to the previous song based on play mode'''
        if self.play_pl is None or not self.play_pl.path_list:
            raise ValueError("No playlist or songs available")
        
        if self.play_mode == PLAY_MODE.ONE:
            return self.curr_song if self.curr_song else self.load_song(0)
        
        if self.play_mode == PLAY_MODE.MIX:
            import random
            self.index = random.randint(0, len(self.play_pl.path_list) - 1)
        else:
            self.index = (self.index - 1 + len(self.play_pl.path_list)) % len(self.play_pl.path_list)
        
        return self.load_song(self.index)

    def set_edit_pl(self, path: str):
        '''Set the playlist for editing'''
        try:
            self.edit_pl = Playlist(path)
            self.e_edit_pl.trigger()
        except Exception as e:
            print(f"Error setting edit playlist: {e}")

    def add_song(self, *paths: str):
        '''Add songs to the editing playlist'''
        if self.edit_pl is None:
            return
        
        self.edit_pl.add_song(*paths)
        self.__e_pl_trigger()

    def remove_song(self, *index: int):
        '''Remove songs from the editing playlist'''
        if self.edit_pl is None:
            return
        
        self.edit_pl.remove_song(*index)
        self.__e_pl_trigger()

    def insert_song(self, up_down: bool, target: int, *index: int):
        '''Insert or move songs in the editing playlist'''
        if self.edit_pl is None:
            return
        
        self.edit_pl.insert_song(up_down, target, *index)
        self.__e_pl_trigger()

    def create(self, name: str):
        '''Create a new playlist'''
        self.pl_list.create(name)
        self.e_pl_list.trigger()

    def update(self, name_or_index: Union[str, int], new_name: str):
        '''Update a playlist name'''
        self.pl_list.update(name_or_index, new_name)
        self.e_pl_list.trigger()

    def delete(self, name_or_index: Union[str, int]):
        '''Delete a playlist'''
        self.pl_list.delete(name_or_index)
        self.e_pl_list.trigger()

    def __e_pl_trigger(self):
        '''Trigger playlist-related events'''
        self.e_edit_pl.trigger()
        if self.edit_pl == self.play_pl: 
            self.e_play_pl.trigger()
