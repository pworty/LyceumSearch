import sqlite3
import sys
from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QTableWidgetItem

from CodeTest import CodeTest
from Tutorial import Tutorial
from DBUpdater import DBUpdater
from ResetDialog import ResetDialog


# TODO: move methods to standalone files

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("settings.txt", "r") as f:
            data = f.readlines()
        self.SHOW_TUTORIAL, self.DB_NAME = [d.split(' = ')[1].split('\n')[0] for d in data]
        self.SHOW_TUTORIAL = int(self.SHOW_TUTORIAL)
        self.SECTION = 'ALL'
        self.TYPE = 'PROBLEM'
        self.initUI()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)
        self.center()
        self.show()

        self.openTutorial('launch')

        self.btnSearch.clicked.connect(self.search)

        self.actionProblems_All.triggered.connect(partial(self.changeSection, 'ALL', 'PROBLEM'))
        self.actionStudentsBook_All.triggered.connect(partial(self.changeSection, 'ALL', 'BOOK'))
        self.actionLessons_All.triggered.connect(partial(self.changeSection, 'ALL', 'LESSON'))
        self.actionIndependentWorks_All.triggered.connect(
            partial(self.changeSection, 'ALL', 'IWORK'))
        self.actionTests_All.triggered.connect(partial(self.changeSection, 'ALL', 'TEST'))

        self.actionProblems_FY.triggered.connect(partial(self.changeSection, 'FY', 'PROBLEM'))
        self.actionStudentsBook_FY.triggered.connect(partial(self.changeSection, 'FY', 'BOOK'))
        self.actionLessons_FY.triggered.connect(partial(self.changeSection, 'FY', 'LESSON'))
        self.actionIndependentWorks_FY.triggered.connect(partial(self.changeSection, 'FY', 'IWORK'))
        self.actionTests_FY.triggered.connect(partial(self.changeSection, 'FY', 'TEST'))

        self.actionProblems_SY.triggered.connect(partial(self.changeSection, 'SY', 'PROBLEM'))
        self.actionStudentsBook_SY.triggered.connect(partial(self.changeSection, 'SY', 'BOOK'))
        self.actionLessons_SY.triggered.connect(partial(self.changeSection, 'SY', 'LESSON'))

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
        # TODO: improve search algorithm
        # TODO: maybe remove id from database display
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()
            search = self.plainTextSearchField.toPlainText()
            query = f"""SELECT * FROM {self.DB_NAME} 
                    WHERE (Name LIKE '%{search}%' OR Keywords LIKE '%{search}%')"""
            if self.SECTION == 'ALL':
                query += f"""AND Type = '{self.TYPE.lower()}';"""
            elif self.SECTION == 'FY':
                query += f"""AND Type = '{self.TYPE.lower()}' AND Year = 1;"""
            elif self.SECTION == 'SY':
                query += f"""AND Type = '{self.TYPE.lower()}' AND Year = 2;"""
            data = cur.execute(query).fetchall()
            self.tableWidgetResults.setRowCount(0)
            for i, row in enumerate(data):
                self.tableWidgetResults.setRowCount(self.tableWidgetResults.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidgetResults.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidgetResults.resizeColumnsToContents()
        except sqlite3.Error as error:
            self.plainTextSearchField.appendPlainText(str(error))
        finally:
            if con:
                con.close()

    def changeSection(self, section, type):
        '''
        Search section change (All problems, Students book, Themes, Independent works, Tests)
        Изменение секции поиска (Все задачи, Учебник, Темы, Самостоятельные, Контрольные)
        :return:
        '''
        self.SECTION = section
        self.TYPE = type

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
