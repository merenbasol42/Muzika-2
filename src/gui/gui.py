import customtkinter as ctk
from .header import Header
from .pages.edit_page import EditPage
from .pages.play_page import PlayPage
from .pages import IPage

SIZE = (450, 600)

class IUI:
    # Singleton
    __instance = None
    def __init__(self):
        if IUI.__instance is None:
            IUI.__instance = self
        else:
            return IUI.__instance

    def run(self):
        pass

class GUI(IUI):
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        self.root.title("Muzika")
        self.root.geometry(f"{SIZE[0]}x{SIZE[1]}")
        self.root.resizable(True, True) # False, False
        self.header: Header
        self.edit_page: EditPage
        self.play_page: PlayPage
        self.curr_page: IPage

    def run(self):
        self.init_components()
        self.root.mainloop()

    def init_components(self):
        self.header = Header(self.root)
        self.header.create()
        self.header.insert()
        self.header.pack(side="top", fill='x')
        
        self.edit_page = EditPage(self.root)
        self.header.create()
        self.header.insert()
        self.header.pack(side="top", fill='x')
        
        self.play_page = PlayPage(self.root)
        self.play_page.create()
        self.play_page.insert()
        self.play_page.pack(side="top", fill='x')