import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from DBInteraction import DBInteraction


class Main(QMainWindow, DBInteraction):
    from Center import center
    from globals import globalsInit
    from UILanguage import langDict, translation_RU, UIRename, changeLanguage
    from buttonsConnect import buttonsConnect
    from Tutorial import openTutorial
    from ResetDialog import resetAll

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)
        self.center()
        self.show()

        self.globalsInit()
        # UI language load
        # Загрузка языка интерфейса
        self.changeLanguage(self.LANGUAGE)

        self.buttonsConnect()

        # TODO: add a tutorial
        # self.openTutorial('launch')

    def keyPressEvent(self, event):
        # TODO: fix not searching by enter while typing in search field
        if event.key() == Qt.Key_Return:
            self.search()
        elif event.key() == Qt.Key_Escape:
            self.close()
        event.accept()

    def closeEvent(self, event):
        '''
        Closes all windows if main is closed

        Закрывает все окна если главное закрыто
        :param event:
        :return:
        '''
        app.closeAllWindows()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Main()
    sys.exit(app.exec())
