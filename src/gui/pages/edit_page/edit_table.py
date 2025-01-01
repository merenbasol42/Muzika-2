import customtkinter as ctk
from mcfg import Configurer
from mguitb import IComponent, Table, IconButton
from mtools import path_works as pw

COLS = ["name", "singer", "length"]

class EditTable(IComponent):
    def __init__(self, master):
        super().__init__(master)
        self.__cfg = Configurer().cfg
        self.table: Table
        self.frame: ctk.CTkFrame
        self.pl_cbox: ctk.CTkComboBox
        self.cre_btn: IconButton
        self.del_btn: IconButton

    def create(self):
        i = pw.add(self.__cfg.icons_dir, "edit_page")
        self.frame = ctk.CTkFrame(self)
        self.cre_btn = IconButton(
            master = self.frame,
            command = self.__cb_cre_btn,
            def_icon_path = pw.add(i, "create.png")
        )
        self.del_btn = IconButton(
            master = self.frame,
            command = self.__cb_del_btn,
            def_icon_path = pw.add(i, "delete.png")
        )
        self.pl_cbox = ctk.CTkComboBox(
            master = self.frame,
            command = self.__cb_pl_cbox,
            values = [],
        )
        self.pl_cbox.set("Set a playlist")

        self.table = Table(self, COLS)
        return super().create()
    
    def insert(self):
        self.cre_btn.grid(row=0, column=0, sticky='nswe')
        self.pl_cbox.grid(row=0, column=1, sticky='nswe')
        self.del_btn.grid(row=0, column=2, sticky='nswe')
        self.frame.grid_columnconfigure(0, weight=2)
        self.frame.grid_columnconfigure(1, weight=5)
        self.frame.grid_columnconfigure(2, weight=2)
        self.frame.grid_rowconfigure(0, weight=1)

        self.frame.grid(row=0, column=0, sticky='nswe')
        self.table.grid(row=1, column=0, sticky='nswe')

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        return super().insert()

    def __cb_pl_cbox(self, item: str):
        print(f"selected {item}")

    def __cb_cre_btn(self):
        pass

    def __cb_del_btn(self):
        pass