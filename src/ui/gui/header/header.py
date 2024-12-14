from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel
)
from ..qwidgets import *

class Header(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent)
        self._page_title_lbl: QLabel = QLabel()
        self._notification_lbl: QLabel = QLabel()
        self._ch_page_btn: QPushButton = QPushButton()
        self._settings_page_btn: QPushButton = QPushButton()


    def build(self):
        VerticalLayout(
            self,
            self._notification_lbl, 
            HorizontalLayout(
                self,
                self._ch_page_btn,
                self._page_title_lbl,
                self._settings_page_btn
            )
        )
        self._ch_page_btn.clicked.connect(
            self.ch_page_btn_clicked_cb
        )
    
    def ch_page_btn_clicked_cb(self, *args):
        print("clicked")
