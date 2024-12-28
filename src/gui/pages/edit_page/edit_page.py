from ..ipage import IPage

class EditPage(IPage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        