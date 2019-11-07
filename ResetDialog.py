from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ResetDialog(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.LANGUAGE = args[1]
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 100)
        uic.loadUi('ResetDialog.ui', self)
        if self.LANGUAGE == 'RU':
            self.labelMessage.setText('Настройки\nбыли сброшены!')
        elif self.LANGUAGE == 'EN':
            self.labelMessage.setText('Your settings\nhave been reset!')
        self.show()


def resetAll(self):
    '''
    Resets all settings to default

    Сбрасывает все настройки на изначальные
    :return:
    '''

    self.resetDialog = ResetDialog(self, self.LANGUAGE)
    with open("defaults.txt", "r") as f:
        data = f.readlines()
    with open('settings.txt', "w") as f:
        f.write(''.join(data))
    self.initUI()
