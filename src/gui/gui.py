import customtkinter as ctk
from .header import Header
from .menu import Menu
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
        self.root: ctk.CTk
        self.menu: Menu
        self.header: Header
        self.edit_page: EditPage
        self.play_page: PlayPage
        self.curr_page: IPage

    def run(self):
        self.__init_window()
        self.__init_components()
        self.root.mainloop()
    
    #
    # Initialize
    #

    def __init_window(self):
        self.root = ctk.CTk()
        self.root.title("Muzika")
        self.root.geometry(f"{SIZE[0]}x{SIZE[1]}")
        self.root.resizable(True, True) # False, False

    def __init_components(self):
        self.__init_header()
        self.__init_menu()
        self.__init_edit_page()
        self.__init_play_page()
    
    def __init_menu(self):
        self.menu = Menu()
        self.menu.withdraw()

    def __init_header(self):
        self.header = Header(self.root)
        self.header.create()
        self.header.insert()
        self.header.navigator.ch_page_button.configure(
            command = self.ch_page
        )
        self.header.navigator.settings_button.configure(
            command = self.display_menu
        )
        self.header.pack(side="top", fill='x')

    def __init_play_page(self):
        self.play_page = PlayPage(self.root)
        self.play_page.create()
        self.play_page.insert()
        self.play_page.configure(fg_color='red')
        self.play_page.pack(side="top", fill='both', expand=True, padx=5, pady=5)
        self.curr_page = self.play_page

    def __init_edit_page(self):
        self.edit_page = EditPage(self.root)
        self.edit_page.create()
        self.edit_page.insert()

    #
    # Callbacks
    #

    def display_menu(self):
        self.menu.iconify()

    def ch_page(self):
        if self.curr_page == self.play_page:
            self.play_page.pack_forget()
            self.edit_page.pack(side="top", fill='both', expand=True, padx=5, pady=5)
            self.curr_page = self.edit_page
        else: # current page is edit_page
            self.edit_page.pack_forget()
            self.play_page.pack(side="top", fill='both', expand=True, padx=5, pady=5)
            self.curr_page = self.play_page
