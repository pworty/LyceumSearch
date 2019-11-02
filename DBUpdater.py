import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QWidget


class DBUpdater(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.DB_NAME = args[1]
        self.initUI()

    def initUI(self):
        uic.loadUi('DBUpdater.ui', self)

        self.pushButtonAddRecord.clicked.connect(self.addRecord)

        self.show()

    def addRecord(self):
        '''
        Adds a record to the database

        Добавляет запись в базу данных
        :return:
        '''
        # TODO: add id displaying after adding a new record
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()

            Name = self.plainTextEditName.toPlainText()
            Year = self.plainTextEditYear.toPlainText()
            Type = self.plainTextEditType.toPlainText()
            Keywords = self.plainTextEditKeywords.toPlainText()
            Link = self.plainTextEditLink.toPlainText()

            cur.execute(f"""INSERT INTO {self.DB_NAME} (Name, Year, Type, Keywords, Link)
            VALUES ('{Name}', {Year}, '{Type}', '{Keywords}', '{Link}');""")
            self.labelRecordAdded.setText(f'Record added!')
            print(cur.execute("""SELECT * FROM lyceumTable;""").fetchall())
        except sqlite3.Error as error:
            self.plainTextEditName.clear()
            self.plainTextEditYear.clear()
            self.plainTextEditType.clear()
            self.plainTextEditKeywords.clear()
            self.plainTextEditLink.clear()
            self.labelRecordAdded.setText(str(error))
        finally:
            if con:
                con.commit()
                con.close()
