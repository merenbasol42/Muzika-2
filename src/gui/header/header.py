import customtkinter as ctk

from ..utils.component import IComponent

from .statment_panel import StatementPanel
from .navigator import Navigator


class Header(IComponent):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.statment_panel = StatementPanel(self)
        self.navigator = Navigator(self)

    def create(self): 
        self.statment_panel.create()
        self.navigator.create()
        return super().create()

    def insert(self):
        self.statment_panel.insert()
        self.statment_panel.pack(side="top", fill='x')
        self.navigator.insert()
        self.navigator.pack(side="top", fill='x')
        return super().insert()
