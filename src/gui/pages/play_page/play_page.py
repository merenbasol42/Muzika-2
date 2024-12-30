from mcfg import Configurer
from mguitb import Table
from ..ipage import IPage
from .player import Player
from .volumer import Volumer

class PlayPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg
        self.table: Table 
        self.player = Player(self) 
        self.volumer = Volumer(self)

    def create(self):
        self.table = Table(self, ["name", "singer", "duration"])
        self.player.create()
        self.volumer.create()
        return super().create()
    
    def insert(self):
        self.volumer.insert()
        self.player.insert()
        
        self.table.grid(row=0, column=0, sticky='nswe')
        self.volumer.grid(row=1, column=0, sticky='nswe')
        self.player.grid(row=2, column=0, sticky='nswe')
        
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        return super().insert()