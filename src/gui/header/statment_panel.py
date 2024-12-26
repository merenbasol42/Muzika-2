import customtkinter as ctk
from ..utils import IComponent, IconButton
from ...utils.configurer import Configurer
from ...utils.path_works import add as pw_add

class StatementPanel(IComponent):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.__cfg = Configurer().cfg
        self.statement_lbl: ctk.CTkLabel
        self.mode_icon: IconButton
        self.pause_icon: IconButton
        #
        # Icon paths
        #
        __dir = pw_add(self.__cfg.icons_dir, "header")
        self.MODE_DEF_ICON_PATH: str = pw_add(__dir, "mode_def.png")
        self.MODE_ONE_ICON_PATH: str = pw_add(__dir, "mode_one.png")
        self.MODE_LOOP_ICON_PATH: str = pw_add(__dir, "mode_loop.png")
        self.MODE_MIX_ICON_PATH: str = pw_add(__dir, "mode_mix.png")
        self.PLAY_ICON_PATH: str = pw_add(__dir, "play.png")
        self.PAUSE_ICON_PATH: str = pw_add(__dir, "pause.png")

    def create(self):
        self.mode_icon = IconButton(
            master = self,
            def_icon_path = self.MODE_DEF_ICON_PATH
        )
        self.statement_lbl = ctk.CTkLabel(
            master = self,
            text = "statement_lbl"
        )
        self.pause_icon = IconButton(
            master = self,
            def_icon_path = self.PAUSE_ICON_PATH
        )
        return super().create()

    def insert(self): 
        self.mode_icon.grid(row=0, column=0, padx=2, pady=2)
        self.statement_lbl.grid(row=0, column=1, padx=2, pady=2)
        self.pause_icon.grid(row=0, column=2, padx=2, pady=2)
        self.grid_columnconfigure(1, weight=1)

        return super().insert()
        