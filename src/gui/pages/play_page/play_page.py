import mtools.path_works as pw
from mguitb import IconButton, HOVER_TYPE
from mcfg import Configurer

from ..ipage import IPage
from .player import Player

class PlayPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg
        self.player = Player(self) 

    def create(self):
        self.player.create()
        return super().create()
    
    def insert(self):
        self.player.insert()
        self.player.pack(side="bottom", fill='x')
        return super().insert()