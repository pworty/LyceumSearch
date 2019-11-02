import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from CodeTest import CodeTest
from Tutorial import Tutorial
from DBUpdater import DBUpdater
from ResetDialog import ResetDialog


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("settings.txt", "r") as f:
            data = f.readlines()
        self.SHOW_TUTORIAL, self.DB_NAME = [d.split(' = ')[1].split('\n')[0] for d in data]
        self.SHOW_TUTORIAL = int(self.SHOW_TUTORIAL)
        self.initUI()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)
        self.center()
        self.show()

        self.openTutorial('launch')

        self.btnSearch.clicked.connect(self.search)

        self.actionAllProblems_All.triggered.connect(self.changeSection)
        self.actionStudentsBook_All.triggered.connect(self.changeSection)
        self.actionThemes_All.triggered.connect(self.changeSection)
        self.actionIndependentWorks_All.triggered.connect(self.changeSection)
        self.actionTests_All.triggered.connect(self.changeSection)

        self.actionAllProblems_FY.triggered.connect(self.changeSection)
        self.actionStudentsBook_FY.triggered.connect(self.changeSection)
        self.actionThemes_FY.triggered.connect(self.changeSection)
        self.actionIndependentWorks_FY.triggered.connect(self.changeSection)
        self.actionTests_FY.triggered.connect(self.changeSection)

        self.actionAllProblems_SY.triggered.connect(self.changeSection)
        self.actionStudentsBook_SY.triggered.connect(self.changeSection)
        self.actionThemes_SY.triggered.connect(self.changeSection)
        self.actionIndependentWorks_SY.triggered.connect(self.changeSection)
        self.actionTests_SY.triggered.connect(self.changeSection)

        self.menuCodeTest.triggered.connect(self.openCodeTest)

        self.actionOpenTutorial.triggered.connect(self.openTutorial)

        self.actionOpenDBUpdater.triggered.connect(self.openDBUpdater)

        self.actionResetAll.triggered.connect(self.resetAll)

        self.actionRussian.triggered.connect(self.changeLanguage)
        self.actionEnglish.triggered.connect(self.changeLanguage)
        self.actionMeme.triggered.connect(self.changeLanguage)

    def search(self):
        '''
        Selected section search (All, First year, Second year)
        Поиск по выбранным секциям (Все, Первый год, Второй год)
        :return:
        '''

        # TODO: add links

        pass

    def changeSection(self):
        '''
        Search section change (All problems, Students book, Themes, Independent works, Tests)
        Изменение секции поиска (Все задачи, Учебник, Темы, Самостоятельные, Контрольные)
        :return:
        '''
        pass

    def openCodeTest(self):
        '''
        Code testing window opening
        Открытие окна тестирования кода
        :return:
        '''
        self.codeTest = CodeTest(self)
        self.codeTest.show()

    def openTutorial(self, e):
        '''
        Display tutorial (or not if disabled)
        Показать обучение (или нет если отключено)
        :return:
        '''

        # TODO: Add actual tutorial

        if e == 'launch':
            self.tutorial = Tutorial(self, self.SHOW_TUTORIAL)
        else:
            self.tutorial = Tutorial(self, 1)

    def openDBUpdater(self):
        '''
        Opens DBUpdater dialog window

        Открывает диалоговое окно для обновления базы данных
        :return:
        '''
        self.dbUpdater = DBUpdater(self, self.DB_NAME)


    def resetAll(self):
        '''
        Resets all settings to default

        Сбрасывает все настройки на изначальные
        :return:
        '''
        with open("defaults.txt", "r") as f:
            data = f.readlines()
        with open('settings.txt', "w") as f:
            f.write(''.join(data))
        self.resetDialog = ResetDialog(self)

    def changeLanguage(self):
        '''
        Ui language change
        Изменение языка интерфейса
        :return:
        '''
        pass

    def center(self):
        # geometry of the main window
        # размеры главного окна
        qr = self.frameGeometry()
        # center point of screen
        # центр экрана
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        # перемещение прямоугольника в центр экрана
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        # верхний левый угол прямоугольника совмещается с главным окном
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = main()
    sys.exit(app.exec())
