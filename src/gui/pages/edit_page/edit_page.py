from ..ipage import IPage
from .edit_table import EditTable

class EditPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.table = EditTable(self)

    def create(self):
        self.table.create()
        return super().create()
    
    def insert(self):
        self.table.insert()
        self.table.grid(row=0, column=0, sticky='nswe')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        return super().insert()
        