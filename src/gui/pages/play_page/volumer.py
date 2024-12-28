import customtkinter as ctk

from mguitb import IComponent

class Volumer(IComponent):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.slider: ctk.CTkSlider
        self.name_lbl: ctk.CTkLabel
        self.val_lbl: ctk.CTkLabel
    
    def create(self):
        self.slider = ctk.CTkSlider(
            master = self,
            command = self.__cb_slider_set
        )
        self.name_lbl = ctk.CTkLabel(
            master = self,
            text = "name_lbl text"
        )
        self.val_lbl = ctk.CTkLabel(
            master = self,
            text = "val_lbl text"
        )
        return super().create()
    
    def insert(self):
        self.name_lbl.grid(row=0, column=0)
        self.slider.grid(row=0, column=1)
        self.val_lbl.grid(row=0, column=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_columnconfigure(2, weight=1)
        return super().insert()

    def __cb_slider_set(self, new_pos: float):
        print(f"slider setted: {new_pos}")