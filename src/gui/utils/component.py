import customtkinter as ctk
from tkinter import Misc

class IComponent(ctk.CTkFrame):
    def __init__(self, master: Misc, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    def create(self): pass
    def insert(self): pass
    def remove(self): pass