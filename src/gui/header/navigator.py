import customtkinter as ctk

from ..utils import IComponent, IconButton, HOVER_TYPE
from ...utils.configurer import Configurer
from ...utils.path_works import add as pw_add

class Navigator(IComponent):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.__cfg = Configurer().cfg
        
        self.__icons_dir = pw_add(self.__cfg.icons_dir, "header")
        self.ch_page_button: IconButton
        self.page_lbl: ctk.CTkLabel
        self.settings_button: IconButton

    def create(self):
        self.ch_page_button = IconButton(
            master = self,
            def_icon_path = pw_add(
                self.__icons_dir, 
                "ch_page"
            ),
            hover = HOVER_TYPE.DARKER 
        )
        self.page_lbl = ctk.CTkLabel(
            master = self,
            text = "page_lbl",
            padx = 31
        )
        self.settings_button = IconButton(
            master = self,
            def_icon_path = pw_add(
                self.__icons_dir, 
                "settings"
            ),
            hover = HOVER_TYPE.DARKER
        )
        return super().create()
    
    def insert(self):
        self.ch_page_button.grid(row=0, column=0)
        self.page_lbl.grid(row=0, column=1)
        self.settings_button.grid(row=0, column=2)
        self.grid_columnconfigure(1, weight=1)
        return super().insert()