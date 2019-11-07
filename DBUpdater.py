import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class DBUpdater(QWidget):
    from Center import center

    def __init__(self, *args):
        super().__init__()
        self.DB_NAME = args[1]
        self.initUI()

    def initUI(self):
        uic.loadUi('DBUpdater.ui', self)
        self.center()

        self.pushButtonAddRecord.clicked.connect(self.addRecord)
        self.pushButtonDeleteRecord.clicked.connect(self.deleteRecord)
        self.pushButtonUpdateValues.clicked.connect(self.updateRecord)
        self.pushButtonClearFields.clicked.connect(self.clearFields)

        self.show()

    def addRecord(self):
        '''
        Adds the record to the database

        Добавляет запись в базу данных
        :return:
        '''
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()

            self.readFields()

            cur.execute(f"""INSERT INTO {self.DB_NAME} (Name, Year, Type, Keywords, Link)
            VALUES ('{self.Name}', {self.Year}, '{self.Type}', '{self.Keywords}', '{self.Link}');""")
            id = \
                cur.execute(f"""SELECT id FROM lyceumTable where Link='{self.Link}'""").fetchall()[
                    0][0]
            self.labelRecordAdded.setText(f'Record with id={id} added!')
        except sqlite3.Error as error:
            self.clearFields()
            self.labelRecordAdded.setText(str(error))
        finally:
            if con:
                con.commit()
                con.close()

    def deleteRecord(self):
        '''
        Deletes the record from the database

        Удаляет запись из базы данных
        :return:
        '''
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()

            self.readFields()
            cur.execute(f"""DELETE FROM {self.DB_NAME} WHERE id = {self.Id};""")

            self.labelRecordAdded.setText(f'Record with id={self.Id} deleted!')
        except sqlite3.Error as error:
            self.clearFields()
            self.labelRecordAdded.setText(str(error))
        finally:
            if con:
                con.commit()
                con.close()

    def updateRecord(self):
        '''
        Updates the record in the database

        Обгновляет запись в базе данных
        :return:
        '''
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()

            self.readFields()

            query = []
            if self.Name:
                query.append(f"""Name = '{self.Name}'""")
            if self.Year:
                query.append(f"""Year = {self.Year}""")
            if self.Type:
                query.append(f"""Type = '{self.Type}'""")
            if self.Keywords:
                query.append(f"""Keywords = '{self.Keywords}'""")
            if self.Link:
                query.append(f"""Link = '{self.Link}'""")
            cur.execute(f"""UPDATE {self.DB_NAME} SET {', '.join(query)} WHERE id = {self.Id};""")

            self.labelRecordAdded.setText(f'Record with id={self.Id} updated!')
        except sqlite3.Error as error:
            self.clearFields()
            self.labelRecordAdded.setText(str(error))
        finally:
            if con:
                con.commit()
                con.close()

    def clearFields(self):
        '''
        Deletes all the text from input fields

        Удаляет весь текст из полей ввода
        :return:
        '''
        self.plainTextEditName.clear()
        self.plainTextEditYear.clear()
        self.plainTextEditType.clear()
        self.plainTextEditKeywords.clear()
        self.plainTextEditLink.clear()
        self.plainTextEditId.clear()

    def readFields(self):
        '''
        Reads user input

        Считывает пользовательский ввод
        :return:
        '''
        self.Name = self.plainTextEditName.toPlainText().strip()
        self.Year = self.plainTextEditYear.toPlainText().strip()
        self.Type = self.plainTextEditType.toPlainText().strip()
        self.Keywords = self.plainTextEditKeywords.toPlainText().strip()
        self.Link = self.plainTextEditLink.toPlainText().strip()
        self.Id = self.plainTextEditId.toPlainText().strip()

        self.clearFields()

        self.plainTextEditName.appendPlainText(self.Name)
        self.plainTextEditYear.appendPlainText(self.Year)
        self.plainTextEditType.appendPlainText(self.Type)
        self.plainTextEditKeywords.appendPlainText(self.Keywords)
        self.plainTextEditLink.appendPlainText(self.Link)
        self.plainTextEditId.appendPlainText(self.Id)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        event.accept()
