from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget


class Tutorial(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.SHOW_TUTORIAL = args

        self.initUI()

    def initUI(self):
        uic.loadUi('Tutorial.ui', self)
        self.checkBoxShowTutorial.stateChanged.connect(self.showTutorial)

    def showTutorial(self, state):
        if state == QtCore.Qt.Checked:
            self.SHOW_TUTORIAL = 0
        else:
            self.SHOW_TUTORIAL = 1
        with open('settings.txt', "w") as f:
            f.write(f'SHOW_TUTORIAL = {self.SHOW_TUTORIAL}')
