from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResetDialog(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('ResetDialog.ui', self)
        self.show()
