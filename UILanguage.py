# Language dictionary
# Dictionary of used words to translate later
# Словарь используемых слов для дальнейшего перевода
langDict = {'Search': '', 'Keywords': '', 'All': '', 'Search problems': '',
            'First year': '', 'Second year': '', 'Problems': '', 'Book': '',
            'Lessons': '', 'Independent works': '', 'Tests': '', 'Other actions': '',
            'Full DB': '', 'Change DB': '', 'Reset all': '', 'Help': '',
            'Open tutorial': '', 'Name': '', 'Year': '', 'Type': '', 'Link': ''}
# Russian translation (default)
# Русский перевод (по умолчанию)
translation_RU = ['Поиск', 'Ключевые слова', 'Все', 'Искать задачи', 'Первый год',
                  'Второй год', 'Задачи', 'Учебник', 'Уроки', 'Самостоятельные',
                  'Контрольные', 'Другие действия', 'Полная БД', 'Изменить БД',
                  'Сбросить все', 'Помощь', 'Открыть обучение', 'Название', 'Год',
                  'Тип', 'Ссылка']
translation_ = ['Поиск', 'Ключевые слова', 'Все', 'Искать задачи', 'Первый год',
                'Второй год', 'Задачи', 'Учебник', 'Уроки', 'Самостоятельные',
                'Контрольные', 'Другие действия', 'Полная БД', 'Изменить БД',
                'Сбросить все', 'Помощь', 'Открыть обучение', 'Название', 'Год',
                'Тип', 'Ссылка']


def UIRename(self):
    '''
    Renames UI to chosen language

    Переименовывает интерфейс на выбранный язык
    :param self:
    :return:
    '''
    self.btnSearch.setText(self.langDict['Search'])
    if self.LANGUAGE == 'RU':
        self.lbKeywords.setText('Ключевые\nслова')
    elif self.LANGUAGE == 'EN':
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


def changeLanguage(self, language):
    '''
    Ui language change

    Изменение языка интерфейса
    :return:
    '''
    self.LANGUAGE = language
    with open("settings.txt", "r") as f:
        data = f.readlines()
    with open('settings.txt', "w") as f:
        f.write(''.join(data[:-1]))
        f.write(f'LANGUAGE = {self.LANGUAGE}\n')

    # Fills the translations in other languages or keys into values if English chosen
    # Заполняет переводы на других языках или ключи в значения если выбран Английский
    for ind, key in enumerate(self.langDict.keys()):
        if self.LANGUAGE == 'RU':
            self.langDict[key] = self.translation_RU[ind]
        elif self.LANGUAGE == 'EN':
            self.langDict[key] = key

    self.UIRename()
