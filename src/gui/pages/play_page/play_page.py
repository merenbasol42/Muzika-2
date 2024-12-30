from mcfg import Configurer

from ..ipage import IPage
from .player import Player
from .volumer import Volumer

class PlayPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg
        self.player = Player(self) 
        self.volumer = Volumer(self)

    def create(self):
        self.player.create()
        self.volumer.create()
        return super().create()
    
    def insert(self):
        self.player.insert()
        self.volumer.insert()
        self.player.pack(side="bottom", fill='x')
        self.volumer.pack(side="bottom", fill='x')
        # self.player.grid(row=0, column=0)
        # self.volumer.grid(row=1, column=0)
        # self.player.grid_columnconfigure(0, weight=1)
        # self.volumer.grid_columnconfigure(0, weight=1)
        # self.player.grid_rowconfigure(0, weight=1)
        # self.volumer.grid_rowconfigure(1, weight=1)

        return super().insert()