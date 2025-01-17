import mtools.path_works as pw 
from mcfg import Configurer
from .gui import GUI

class Program: 
    '''Program class'''
    def __init__(self, ws_path: str):
        self.ws_path = ws_path
        self.__cfg = Configurer(pw.add(ws_path, "config", "config.json"))
        self.gui = GUI()
        
    #
    # Initialize
    #

    def initialize(self):
        '''Initializing program'''
        self.bind()

    def bind(self):
        '''Binding communication channels between backend and frontend'''
        pass

    #
    # Running
    # 

    def pre_run(self):
        '''Pre-starting program'''
        pass

    def run(self):
        print("Running program")
        self.pre_run()
        self.gui.run()