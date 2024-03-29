from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class Tutorial(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.step = 0
        self.SHOW_TUTORIAL = args[1]
        self.initUI()

    def initUI(self):
        uic.loadUi('UIs/Tutorial.ui', self)
        # self.pushButtonNext.clicked.connect(self.nextStep)
        self.checkBoxShowTutorial.stateChanged.connect(self.show_tutorial)
        if self.SHOW_TUTORIAL == 1:
            self.show()

    def show_tutorial(self, state):
        if state == QtCore.Qt.Checked:
            self.SHOW_TUTORIAL = 0
        else:
            self.SHOW_TUTORIAL = 1
        with open("settings.txt", "r") as f:
            data = f.readlines()
        with open('settings.txt', "w") as f:
            f.write(f'SHOW_TUTORIAL = {self.SHOW_TUTORIAL}\n')
            f.write(''.join(data[1:]))

    # TODO: add tutorial images
    # def nextStep(self):
    #   self.step = (self.step + 1) % n

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        event.accept()


def open_tutorial(self, e):
    '''
    Display tutorial (or not if disabled)

    Показать обучение (или нет если отключено)
    :return:
    '''
    if e == 'launch':
        # Show on launch if checked
        # Показать при запуске если стоит галочка
        self.tutorial = Tutorial(self, self.SHOW_TUTORIAL)
    else:
        # Show anyway by press of the 'Open tutorial' button
        # Показать в любом случае по нажатию кнопки 'Открыть обучение'
        self.tutorial = Tutorial(self, 1)
