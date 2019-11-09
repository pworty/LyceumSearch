import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from db_interaction import DBInteraction


class Main(QMainWindow, DBInteraction):
    from center import center
    from globals import globals_init
    from ui_language import langDict, translation_RU, ui_rename, change_language
    from buttons import buttons_connect
    from tutorial_dialog import open_tutorial
    from reset_dialog import reset_all

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UIs/LyceumSearch.ui', self)
        self.center()
        self.show()

        # Global variables load from settings.txt
        # Загрузка глобальных переменных из settings.txt
        self.globals_init()

        # UI language load
        # Загрузка языка интерфейса
        self.change_language(self.LANGUAGE)

        self.buttons_connect()

        # TODO: add a tutorial
        # self.open_tutorial('launch')

    def keyPressEvent(self, event):
        # TODO: fix not searching by enter while typing in search field
        # Search by pressing Enter (on main keyboard)
        # Искать при нажатии Enter (на основной клавиатуре)
        if event.key() == Qt.Key_Return:
            self.search()
        # Close window on Esc press
        # Закрыть окно при нажатии Esc
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
