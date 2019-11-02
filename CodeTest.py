from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class CodeTest(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('CodeTest.ui', self)
        self.show()
