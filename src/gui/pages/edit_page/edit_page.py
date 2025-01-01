from ..ipage import IPage
from .edit_table import EditTable
from .buttons import Buttons

class EditPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.table = EditTable(self)
        self.buttons = Buttons(self)

    def create(self):
        self.table.create()
        self.buttons.create()
        return super().create()
    
    def insert(self):
        self.table.insert()
        self.buttons.insert()
        
        self.table.grid(row=0, column=0, sticky='nswe')
        self.buttons.grid(row=1, column=0, sticky='nswe')
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        return super().insert()
        