import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem

from db_updater_ui import DBUpdater


class DBInteraction:
    def display_results(self, data, ColumnCount, HorizontalHeaderLabels):
        '''
        Displays data in tableWidgetResults

        Отображает информацию в tableWidgetResults
        :return:
        '''
        self.tableWidgetResults.setRowCount(0)
        self.tableWidgetResults.setColumnCount(ColumnCount)
        self.tableWidgetResults.setHorizontalHeaderLabels(HorizontalHeaderLabels)
        for i, row in enumerate(data):
            self.tableWidgetResults.setRowCount(self.tableWidgetResults.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidgetResults.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidgetResults.resizeColumnsToContents()

    def return_results(self, query):
        '''
        Returns the search result for a query

        Возвращает результат поиска по запросу
        :return:
        '''
        try:
            con = sqlite3.connect(self.DB_NAME + '.sqlite')
            cur = con.cursor()
            data = cur.execute(query).fetchall()
            return data
        except sqlite3.Error as error:
            # Print error message into label for user to see it
            # Вывод сообщения об ошибки в надпись для того, чтобы пользователь мог видеть его
            self.plainTextSearchField.appendPlainText(str(error))
        finally:
            if con:
                con.close()

    def change_section(self, section, type):
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

    def search(self):
        '''
        Selected section search (All, First year, Second year)

        Поиск по выбранным секциям (Все, Первый год, Второй год)
        :return:
        '''
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
                query += f""" AND Type = '{self.TYPE.lower()}'"""
            query += """ AND Year = 2;"""
        data = self.return_results(query)
        self.display_results(data, 3,
                             [self.langDict['Name'], self.langDict['Type'], self.langDict['Link']])
        # Only 3 columns are displayed to avoid confusing the user (total of 6)
        # Отображаются только 3 колонки, чтобы пользователь не запутался (всего 6)

        # langDict is used to make the column names' translated
        # langDict используется для перевода названий колнок

    def open_full_db(self):
        '''
        Opens fully detailed DB

        Открывает полную БД со всей информацией
        :return:
        '''
        query = f"""SELECT * FROM {self.DB_NAME};"""
        data = self.return_results(query)
        self.display_results(data, 6,
                             ['id', self.langDict['Name'], self.langDict['Year'],
                             self.langDict['Type'], self.langDict['Keywords'],
                             self.langDict['Link']])

    def open_db_updater(self):
        '''
        Opens DBUpdater dialog window

        Открывает диалоговое окно DBUpdater
        :return:
        '''
        self.dbUpdater = DBUpdater(self, self.DB_NAME)
