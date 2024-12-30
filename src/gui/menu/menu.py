
import customtkinter as ctk

SIZE: tuple[int, int] = (200, 300)

class Menu(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry(f"{SIZE[0]}x{SIZE[1]}")
        self.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.withdraw)
    
    def cb_win_del_button(self):
        self.withdraw()