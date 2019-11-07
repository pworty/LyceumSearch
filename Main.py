import sqlite3
import sys

from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from Tutorial import Tutorial
from DBUpdater import DBUpdater
from ResetDialog import ResetDialog


# TODO: move methods to standalone files

class Main(QMainWindow):
    from Center import center

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)
        self.center()
        self.show()

        # Variables init
        # Инициализация переменных
        with open("settings.txt", "r") as f:
            data = f.readlines()
        self.SHOW_TUTORIAL, self.DB_NAME, self.LANGUAGE = [d.split(' = ')[1].split('\n')[0] for d in
                                                           data]
        self.SHOW_TUTORIAL = int(self.SHOW_TUTORIAL)

        # Language dictionary
        # Dictionary of used words to translate later
        # Словарь используемых слов для дальнейшего перевода
        self.langDict = {'Search': '', 'Keywords': '', 'All': '', 'Search problems': '',
                         'First year': '', 'Second year': '', 'Problems': '', 'Book': '',
                         'Lessons': '', 'Independent works': '', 'Tests': '', 'Other actions': '',
                         'Full DB': '', 'Change DB': '', 'Reset all': '', 'Help': '',
                         'Open tutorial': '', 'Name': '', 'Year': '', 'Type': '', 'Link': ''}
        # Russian translation (default)
        # Русский перевод (по умолчанию)
        self.translation_RU = ['Поиск', 'Ключевые слова', 'Все', 'Искать задачи', 'Первый год',
                               'Второй год', 'Задачи', 'Учебник', 'Уроки', 'Самостоятельные',
                               'Контрольные', 'Другие действия', 'Полная БД', 'Изменить БД',
                               'Сбросить все', 'Помощь', 'Открыть обучение', 'Название', 'Год',
                               'Тип', 'Ссылка']

        self.SECTION = 'ALL'
        self.TYPE = 'ALL'

        # UI language load
        # Загрузка языка интерфейса
        self.changeLanguage(self.LANGUAGE)

        self.openTutorial('launch')

        # Buttons connection
        # Подключение кнопок
        self.btnSearch.clicked.connect(self.search)

        self.actionProblems_All.triggered.connect(partial(self.changeSection, 'ALL', 'PROBLEM'))
        self.actionStudentsBook_All.triggered.connect(partial(self.changeSection, 'ALL', 'BOOK'))
        self.actionLessons_All.triggered.connect(partial(self.changeSection, 'ALL', 'LESSON'))
        self.actionIndependentWorks_All.triggered.connect(
            partial(self.changeSection, 'ALL', 'IWORK'))
        self.actionTests_All.triggered.connect(partial(self.changeSection, 'ALL', 'TEST'))
        self.actionAll_All.triggered.connect(partial(self.changeSection, 'ALL', 'ALL'))

        self.actionProblems_FY.triggered.connect(partial(self.changeSection, 'FY', 'PROBLEM'))
        self.actionStudentsBook_FY.triggered.connect(partial(self.changeSection, 'FY', 'BOOK'))
        self.actionLessons_FY.triggered.connect(partial(self.changeSection, 'FY', 'LESSON'))
        self.actionIndependentWorks_FY.triggered.connect(partial(self.changeSection, 'FY', 'IWORK'))
        self.actionTests_FY.triggered.connect(partial(self.changeSection, 'FY', 'TEST'))
        self.actionAll_FY.triggered.connect(partial(self.changeSection, 'FY', 'ALL'))

        self.actionProblems_SY.triggered.connect(partial(self.changeSection, 'SY', 'PROBLEM'))
        self.actionStudentsBook_SY.triggered.connect(partial(self.changeSection, 'SY', 'BOOK'))
        self.actionLessons_SY.triggered.connect(partial(self.changeSection, 'SY', 'LESSON'))
        self.actionAll_SY.triggered.connect(partial(self.changeSection, 'SY', 'ALL'))

        self.actionOpenTutorial.triggered.connect(self.openTutorial)

        self.actionOpenFullDB.triggered.connect(self.openFullDB)

        self.actionOpenDBUpdater.triggered.connect(self.openDBUpdater)

        self.actionResetAll.triggered.connect(self.resetAll)

        self.actionRussian.triggered.connect(partial(self.changeLanguage, 'RU'))
        self.actionEnglish.triggered.connect(partial(self.changeLanguage, 'EN'))

    def search(self):
        '''
        Selected section search (All, First year, Second year)

        Поиск по выбранным секциям (Все, Первый год, Второй год)
        :return:
        '''
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()

            # Getting the user query
            # Получение пользовательского запроса
            search = self.plainTextSearchField.toPlainText().strip()

            # User query formatting (only visual)
            # Форматирование запроса (только визуальное)
            self.plainTextSearchField.clear()
            self.plainTextSearchField.appendPlainText(search)

            # DB print by query
            # Вывод БД по запросу
            query = f"""SELECT Name, Type, Link FROM {self.DB_NAME}
                    WHERE ((Name LIKE '%{search}%' OR Name LIKE '%{search.capitalize()}%')
                    OR (Keywords LIKE '%{search}%' OR Keywords LIKE '%{search.capitalize()}%'))"""
            if self.SECTION == 'ALL':
                if self.TYPE != 'ALL':
                    query += f""" AND Type = '{self.TYPE.lower()}';"""
            elif self.SECTION == 'FY':
                if self.TYPE != 'ALL':
                    query += f""" AND Type = '{self.TYPE.lower()}'"""
                query += """AND Year = 1;"""
            elif self.SECTION == 'SY':
                if self.TYPE != 'ALL':
                    query += f"""AND Type = '{self.TYPE.lower()}"""
                query += """ AND Year = 2;"""
            data = cur.execute(query).fetchall()
            self.tableWidgetResults.setRowCount(0)

            # Only 3 columns are displayed to avoid confusing the user (total of 6)
            # Отображаются только 3 колонки, чтобы пользователь не запутался (всего 6)
            self.tableWidgetResults.setColumnCount(3)

            # langDict is used to make the column names' translated
            # langDict используется для перевода названий колнок
            self.tableWidgetResults.setHorizontalHeaderLabels(
                [self.langDict['Name'], self.langDict['Type'], self.langDict['Link']])
            for i, row in enumerate(data):
                self.tableWidgetResults.setRowCount(self.tableWidgetResults.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidgetResults.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidgetResults.resizeColumnsToContents()
        except sqlite3.Error as error:
            # Print error message into label for user to see it
            # Вывод сообщения об ошибки в надпись для того, чтобы пользователь мог видеть его
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

        text = ''
        if self.TYPE == 'PROBLEM':
            text = self.langDict['Problems']
        elif self.TYPE == 'BOOK':
            text = self.langDict['Book']
        elif self.TYPE == 'LESSON':
            text = self.langDict['Lessons']
        elif self.TYPE == 'IWORK':
            text = self.langDict['Independent works']
        elif self.TYPE == 'TEST':
            text = self.langDict['Tests']
        elif self.TYPE == 'ALL':
            text = self.langDict['All']

        if self.SECTION == 'ALL':
            self.lblSection.setText(f'{text}')
        elif self.SECTION == 'FY':
            self.lblSection.setText(f'{text} ({self.langDict["First year"]})')
        elif self.SECTION == 'SY':
            self.lblSection.setText(f'{text} ({self.langDict["Second year"]})')

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

    def openFullDB(self):
        '''
        Opens fully detailed DB

        Открывает полную БД со всей информацией
        :return:
        '''
        con = sqlite3.connect(self.DB_NAME + '.sqlite')
        cur = con.cursor()

        data = cur.execute(f"""SELECT * from {self.DB_NAME}""").fetchall()
        self.tableWidgetResults.setRowCount(0)
        self.tableWidgetResults.setColumnCount(6)
        self.tableWidgetResults.setHorizontalHeaderLabels(
            ['id', self.langDict['Name'], self.langDict['Year'], self.langDict['Type'],
             self.langDict['Keywords'], self.langDict['Link']])
        for i, row in enumerate(data):
            self.tableWidgetResults.setRowCount(self.tableWidgetResults.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidgetResults.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidgetResults.resizeColumnsToContents()

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

        self.resetDialog = ResetDialog(self, self.LANGUAGE)
        with open("defaults.txt", "r") as f:
            data = f.readlines()
        with open('settings.txt', "w") as f:
            f.write(''.join(data))
        self.initUI()

    def changeLanguage(self, language):
        '''
        Ui language change

        Изменение языка интерфейса
        :return:
        '''
        # Fills the translations in other languages or keys into values if English chosen
        # Заполняет переводы на других языках или ключи в значения если выбран Английский
        for ind, key in enumerate(self.langDict.keys()):
            if language == 'RU':
                self.langDict[key] = self.translation_RU[ind]
            elif language == 'EN':
                self.langDict[key] = key

        # Program elements renaming to chosen language
        # Переименование элементов програм на выбранный
        self.btnSearch.setText(self.langDict['Search'])
        if language == 'RU':
            self.lbKeywords.setText('Ключевые\nслова')
        elif language == 'EN':
            self.lbKeywords.setText(self.langDict['Keywords'])
        self.lblSection.setText(self.langDict['All'])
        self.tableWidgetResults.setHorizontalHeaderLabels(
            [self.langDict['Name'], self.langDict['Type'], self.langDict['Link']])

        self.menuSearchProblems.setTitle(self.langDict['Search problems'])

        self.menuAll.setTitle(self.langDict['All'])
        self.actionProblems_All.setText(self.langDict['Problems'])
        self.actionStudentsBook_All.setText(self.langDict['Book'])
        self.actionLessons_All.setText(self.langDict['Lessons'])
        self.actionIndependentWorks_All.setText(self.langDict['Independent works'])
        self.actionTests_All.setText(self.langDict['Tests'])
        self.actionAll_All.setText(self.langDict['All'])

        self.menuFirstYear.setTitle(self.langDict['First year'])
        self.actionProblems_FY.setText(self.langDict['Problems'])
        self.actionStudentsBook_FY.setText(self.langDict['Book'])
        self.actionLessons_FY.setText(self.langDict['Lessons'])
        self.actionIndependentWorks_FY.setText(self.langDict['Independent works'])
        self.actionTests_FY.setText(self.langDict['Tests'])
        self.actionAll_FY.setText(self.langDict['All'])

        self.menuSecondYear.setTitle(self.langDict['Second year'])
        self.actionProblems_SY.setText(self.langDict['Problems'])
        self.actionStudentsBook_SY.setText(self.langDict['Book'])
        self.actionLessons_SY.setText(self.langDict['Lessons'])
        self.actionAll_SY.setText(self.langDict['All'])

        self.menuOtherActions.setTitle(self.langDict['Other actions'])
        self.actionOpenFullDB.setText(self.langDict['Full DB'])
        self.actionOpenDBUpdater.setText(self.langDict['Change DB'])
        self.actionResetAll.setText(self.langDict['Reset all'])

        self.menuHelp.setTitle(self.langDict['Help'])
        self.actionOpenTutorial.setText(self.langDict['Open tutorial'])

        self.LANGUAGE = language
        with open("settings.txt", "r") as f:
            data = f.readlines()
        with open('settings.txt', "w") as f:
            f.write(''.join(data[:-1]))
            f.write(f'LANGUAGE = {self.LANGUAGE}\n')


    def closeEvent(self, event):
        """
        Closes all windows if main is closed

        Закрывает все окна если главное закрыто
        :param event:
        :return:
        """
        app.closeAllWindows()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Main()
    sys.exit(app.exec())
