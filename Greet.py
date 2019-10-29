from PyQt5.QtWidgets import QWidget


class Greet(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi('Greet.ui', self)
