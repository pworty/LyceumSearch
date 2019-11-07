from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget


class Tutorial(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.SHOW_TUTORIAL = args[1]

        self.initUI()

    def initUI(self):
        uic.loadUi('Tutorial.ui', self)
        self.checkBoxShowTutorial.stateChanged.connect(self.showTutorial)
        if self.SHOW_TUTORIAL == 1:
            self.show()

    def showTutorial(self, state):
        if state == QtCore.Qt.Checked:
            self.SHOW_TUTORIAL = 0
        else:
            self.SHOW_TUTORIAL = 1
        with open("settings.txt", "r") as f:
            data = f.readlines()
        with open('settings.txt', "w") as f:
            f.write(f'SHOW_TUTORIAL = {self.SHOW_TUTORIAL}\n')
            f.write(''.join(data[1:]))

    def openTutorial(self, e):
        '''
        Display tutorial (or not if disabled)

        Показать обучение (или нет если отключено)
        :return:
        '''
        # TODO: Add actual tutorial

        if e == 'launch':
            # Show on launch if checked
            # Показать при запуске если стоит галочка
            self.tutorial = Tutorial(self, self.SHOW_TUTORIAL)
        else:
            # Show anyway by press of the 'Open tutorial' button
            # Показать в любом случае по нажатию кнопки 'Открыть обучение'
            self.tutorial = Tutorial(self, 1)

