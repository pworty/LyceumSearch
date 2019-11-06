from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResetDialog(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.LANGUAGE = args[1]
        self.initUI()

    def initUI(self):
        uic.loadUi('ResetDialog.ui', self)
        if self.LANGUAGE == 'RU':
            self.labelMessage.setText('Настройки\nбыли сброшены!')
        elif self.LANGUAGE == 'EN':
            self.labelMessage.setText('Your settings\nhave been reset!')
        self.show()
