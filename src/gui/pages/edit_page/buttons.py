import customtkinter as ctk
from mcfg import Configurer 
from mguitb import IComponent
from mtools import path_works as pw

class Buttons(IComponent):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg
        self.add_btn: ctk.CTkButton
        self.rem_btn: ctk.CTkButton
        self.utube_btn: ctk.CTkButton

    def create(self):
        self.add_btn = ctk.CTkButton(
            master = self,
            text = "add",
            command = self.__cb_add_btn
        )
        self.rem_btn = ctk.CTkButton(
            master = self,
            text = "remove",
            command = self.__cb_rem_btn
        )
        self.utube_btn = ctk.CTkButton(
            master = self,
            text = "utube",
            command = self.__cb_utube_btn
        )
        return super().create()
    
    def insert(self):
        self.add_btn.grid(row=0, column=0)
        self.rem_btn.grid(row=0, column=1)
        self.utube_btn.grid(row=0, column=2)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(0, weight=1)
        return super().insert()

    def __cb_add_btn(self):
        pass

    def __cb_rem_btn(self):
        pass

    def __cb_utube_btn(self):
        pass