import sqlite3
import sys

from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from DBInteraction import DBInteraction
from Tutorial import Tutorial
from ResetDialog import ResetDialog


# TODO: move methods to standalone files
# TODO: review docs

class Main(QMainWindow, DBInteraction):
    from Center import center
    from globals import SHOW_TUTORIAL, DB_NAME, LANGUAGE, SECTION, TYPE
    from UILanguage import langDict, translation_RU
    from buttonsConnect import buttonsConnect

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('LyceumSearch.ui', self)
        self.center()
        self.show()
        
        # UI language load
        # Загрузка языка интерфейса
        self.changeLanguage(self.LANGUAGE)

        self.openTutorial('launch')

        # Buttons connection
        # Подключение кнопок
        self.buttonsConnect()

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
