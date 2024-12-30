import mtools.path_works as pw
from mguitb import IComponent, IconButton, HOVER_TYPE
from mcfg import Configurer

class Player(IComponent):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg
        self.backward_button: IconButton
        self.rewind_button: IconButton
        self.play_button: IconButton
        self.towind_button: IconButton
        self.forward_button: IconButton

    def create(self):
        __dir = pw.add(self.__cfg.icons_dir, "play_page")
        self.backward_button = IconButton(
            master = self,
            def_icon_path = pw.add(__dir, "backward.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.rewind_button = IconButton(
            master = self,
            def_icon_path = pw.add(__dir, "rewind.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.play_button = IconButton(
            master = self,
            def_icon_path = pw.add(__dir, "play.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.towind_button = IconButton(
            master = self,
            def_icon_path = pw.add(__dir, "towind.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.forward_button = IconButton(
            master = self,
            def_icon_path = pw.add(__dir, "forward.png"),
            hover = HOVER_TYPE.DARKER
        )
        return super().create()

    def insert(self):
        self.backward_button.grid(row=0, column=0, sticky='ns')
        self.rewind_button.grid(row=0, column=1, sticky='ns')
        self.play_button.grid(row=0, column=2, sticky='ns')
        self.towind_button.grid(row=0, column=3, sticky='ns')
        self.forward_button.grid(row=0, column=4, sticky='ns')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)

        return super().insert()