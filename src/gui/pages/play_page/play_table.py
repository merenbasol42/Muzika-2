import customtkinter as ctk
from mguitb import IComponent, Table

COLS = ["name", "singer", "length"]

class PlayTable(IComponent):
    def __init__(self, master):
        super().__init__(master)
        self.table: Table
        self.cbox: ctk.CTkComboBox

    def create(self):
        self.table = Table(self, COLS)
        self.cbox = ctk.CTkComboBox(
            master = self,
            command = self.__cb_cbox_selected,
            values = [],
        )
        self.cbox.set("Set a playlist")
        return super().create()
    
    def insert(self):
        self.cbox.grid(row=0, column=0, sticky='nswe')
        self.table.grid(row=1, column=0, sticky='nswe')
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        return super().insert()

    def __cb_cbox_selected(self, item: str):
        print(f"selected {item}")