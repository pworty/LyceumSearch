import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from CodeTest import CodeTest
from Tutorial import Tutorial
from ResetDialog import ResetDialog



class main(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("settings.txt", "r") as f:
            data = f.readlines()
        self.SHOW_TUTORIAL, = [int(d.split(' = ')[1].split('\n')[0]) for d in data]
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

        # To-do:
        # - Add links

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

        # To-do:
        # - Add actual tutorial

        if e == 'launch':
            self.tutorial = Tutorial(self, self.SHOW_TUTORIAL)
        else:
            self.tutorial = Tutorial(self, 1)

    def resetAll(self):
        '''
        Resets all settings to default

        Сбрасывает все настройки на изначальные
        :return:
        '''

        # To-do:
        # - Maybe add defaults.txt file

        with open('settings.txt', "w") as f:
            f.write(f'SHOW_TUTORIAL = 1')
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
