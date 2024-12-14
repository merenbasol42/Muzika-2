import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from .config import window as WIN_CFG
from .header import Header

class GUIMain:
    def __init__(self, argv):
        super().__init__()
        #
        #
        #
        self.app = QApplication(argv)
        self.win = QMainWindow()
        self.win.setWindowTitle(WIN_CFG.TITLE)
        self.win.setGeometry(0, 0, WIN_CFG.WIDTH, WIN_CFG.HEIGHT)
        #
        #
        #
        self.header: Header = Header(self.win)

    def load(self):
        self.header.build()

    def run(self):
        self.load()
        self.win.show()
        sys.exit(
            self.app.exec_()
        )