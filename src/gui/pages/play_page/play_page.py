from ..ipage import IPage
from ...utils import IconButton, HOVER_TYPE
from ....utils.configurer import Configurer
from ....utils.path_works import add as pw_add

class PlayPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__cfg = Configurer().cfg

        self.backward_button: IconButton
        self.rewind_button: IconButton
        self.play_button: IconButton
        self.towind_button: IconButton
        self.forward_button: IconButton

    def create(self):
        __dir = pw_add(self.__cfg.icons_dir, "play_page")
        self.backward_button = IconButton(
            master = self,
            def_icon_path = pw_add(__dir, "backward.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.rewind_button = IconButton(
            master = self,
            def_icon_path = pw_add(__dir, "rewind.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.play_button = IconButton(
            master = self,
            def_icon_path = pw_add(__dir, "play.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.towind_button = IconButton(
            master = self,
            def_icon_path = pw_add(__dir, "towind.png"),
            hover = HOVER_TYPE.DARKER
        )
        self.forward_button = IconButton(
            master = self,
            def_icon_path = pw_add(__dir, "forward.png"),
            hover = HOVER_TYPE.DARKER
        )
        return super().create()
    
    def insert(self):
        self.backward_button.grid(row=0, columns=0)
        self.rewind_button.grid(row=0, columns=1)
        self.play_button.grid(row=0, columns=2)
        self.towind_button.grid(row=0, columns=3)
        self.forward_button.grid(row=0, columns=4)
        return super().insert()