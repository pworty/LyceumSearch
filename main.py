import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

import Greet
import CodeTest


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def Greet(self):
        self.greet = Greet(self)
        self.greet.show()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)

        self.Greet()

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

        self.actionRussian.triggered.connect(self.changeLanguage)
        self.actionEnglish.triggered.connect(self.changeLanguage)
        self.actionMeme.triggered.connect(self.changeLanguage)

        self.center()
        self.show()

    def search(self):
        '''
        Selected section search (All, First year, Second year)
        Поиск по выбранным секциям (Все, Первый год, Второй год)
        :return:
        '''
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
