import customtkinter as ctk
from tkinter import Misc
from os.path import join, exists
from PIL import Image, ImageEnhance
from enum import Enum

class HOVER_TYPE(Enum):
    DARKER = "__darker__"
    LIGHTER = "__lighter__"

DARKER_ENCHANCE = 0.5
LIGHTER_ENCHANCE = 2.0

class IconButton(ctk.CTkButton):
    def __init__(
        self,
        master: Misc,
        def_icon_path: str,
        hover: HOVER_TYPE | str | None = None,
        size: tuple = (20, 20),
        command = None
    ):
        ''' <hover> parametresine "darker", "lighter" veya başka bir resim için ise icon path girebilirsiniz(def_icon_path ile aynı şekilde)'''

        self.def_icon: ctk.CTkImage = None
        self.hover_icon: ctk.CTkImage = None
        self.flag: bool = False

        self.__init_new_icon(
            def_path=def_icon_path,
            hover=hover,
            size=size
        )

        super().__init__(
            master = master,
            text = "",
            width = 0,
            height = 0,
            bg_color = "transparent",
            fg_color = "transparent",
            command = command,
            image = self.def_icon
        )

        self._event_binding()

    def config_icon(
        self,
        new_def_path: str,
        new_hover: HOVER_TYPE | str | None = None, 
        size=(20, 20)
    ):
        ''' <hover> parametresine "darker", "lighter" veya başka bir resim için ise icon path girebilirsiniz(def_icon_path ile aynı şekilde)'''
        self.__init_new_icon(new_def_path, new_hover, size=size)
        self.configure(image=self.def_icon)

    def __init_new_icon(
        self,
        def_path: str | None = None,
        hover: HOVER_TYPE | str | None = None,
        size = (20, 20)
    ):
        ''' <hover> parametresine "darker", "lighter" veya başka bir resim için ise icon path girebilirsiniz(def_icon_path ile aynı şekilde)'''

        dimg = None
        if def_path is not None and exists(def_path): 
            dimg = Image.open(def_path)
        else: 
            dimg = create_no_img()
            print(f"No image from {def_path}")

        himg = None
        match hover:
            case HOVER_TYPE.DARKER: # hover is darker
                himg = ImageEnhance.Brightness(dimg
                ).enhance(DARKER_ENCHANCE)
            case HOVER_TYPE.LIGHTER: # hover is lighter
                himg = ImageEnhance.Brightness(dimg
                ).enhance(LIGHTER_ENCHANCE)
            case None: # hover is None
                himg = dimg
            case _: # hover is a path
                hover = hover if exists(hover) else def_path
                himg = Image.open(hover)

        self.def_icon = ctk.CTkImage(dimg, size=size)
        self.hover_icon = ctk.CTkImage(himg, size=size)

    def _event_binding(self):
        self.bind("<Leave>", self._on_leave)
        self.bind("<Enter>", self._on_enter)

    def _on_leave(self, event=None):
        self.configure(image=self.def_icon)

    def _on_enter(self, event=None):
        self.configure(image=self.hover_icon)


def create_no_img(size=(20, 20)):
    img = Image.new('RGB', size)
    for i in range(size[0]):
        for j in range(size[1]):
            if (i // 10) % 2 == (j // 10) % 2:
                img.putpixel((i, j), (0, 0, 0))
            else:
                img.putpixel((i, j), (255, 255, 255))
    return img