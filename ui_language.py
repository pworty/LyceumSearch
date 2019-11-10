# Language dictionary
# Dictionary of used words to translate later
# Словарь используемых слов для дальнейшего перевода
lang_dict = {'Search': '', 'Keywords': '', 'All': '', 'Search problems': '',
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


def ui_rename(self):
    '''
    Renames UI to chosen language
    (Executed by changeLanguage() method)

    Переименовывает интерфейс на выбранный язык
    (Запускается методом changeLanguage())
    :param self:
    :return:
    '''
    self.btnSearch.setText(self.lang_dict['Search'])
    if self.LANGUAGE == 'RU':
        self.lbKeywords.setText('Ключевые\nслова')
    elif self.LANGUAGE == 'EN':
        self.lbKeywords.setText(self.lang_dict['Keywords'])
    self.lblSection.setText(self.lang_dict['All'])
    self.tableWidgetResults.setHorizontalHeaderLabels(
        [self.lang_dict['Name'], self.lang_dict['Type'], self.lang_dict['Link']])

    self.menuSearchProblems.setTitle(self.lang_dict['Search problems'])

    self.menuAll.setTitle(self.lang_dict['All'])
    self.actionProblems_All.setText(self.lang_dict['Problems'])
    self.actionStudentsBook_All.setText(self.lang_dict['Book'])
    self.actionLessons_All.setText(self.lang_dict['Lessons'])
    self.actionIndependentWorks_All.setText(self.lang_dict['Independent works'])
    self.actionTests_All.setText(self.lang_dict['Tests'])
    self.actionAll_All.setText(self.lang_dict['All'])

    self.menuFirstYear.setTitle(self.lang_dict['First year'])
    self.actionProblems_FY.setText(self.lang_dict['Problems'])
    self.actionStudentsBook_FY.setText(self.lang_dict['Book'])
    self.actionLessons_FY.setText(self.lang_dict['Lessons'])
    self.actionIndependentWorks_FY.setText(self.lang_dict['Independent works'])
    self.actionTests_FY.setText(self.lang_dict['Tests'])
    self.actionAll_FY.setText(self.lang_dict['All'])

    self.menuSecondYear.setTitle(self.lang_dict['Second year'])
    self.actionProblems_SY.setText(self.lang_dict['Problems'])
    self.actionStudentsBook_SY.setText(self.lang_dict['Book'])
    self.actionLessons_SY.setText(self.lang_dict['Lessons'])
    self.actionAll_SY.setText(self.lang_dict['All'])

    self.menuOtherActions.setTitle(self.lang_dict['Other actions'])
    self.actionOpenFullDB.setText(self.lang_dict['Full DB'])
    self.actionOpenDBUpdater.setText(self.lang_dict['Change DB'])
    self.actionResetAll.setText(self.lang_dict['Reset all'])

    self.menuHelp.setTitle(self.lang_dict['Help'])
    self.actionOpenTutorial.setText(self.lang_dict['Open tutorial'])


def change_language(self, language):
    '''
    Ui language change

    Изменение языка интерфейса
    :return:
    '''
    self.LANGUAGE = language
    # Update language in settings.txt
    # Обновить язык в settings.txt
    with open("settings.txt", "r") as f:
        data = f.readlines()
    with open('settings.txt', "w") as f:
        f.write(''.join(data[:-1]))
        f.write(f'LANGUAGE = {self.LANGUAGE}\n')

    # Fills the translations in other languages or keys into values if English chosen
    # Заполняет переводы на других языках или ключи в значения если выбран Английский
    for ind, key in enumerate(self.lang_dict.keys()):
        if self.LANGUAGE == 'RU':
            self.lang_dict[key] = self.translation_RU[ind]
        elif self.LANGUAGE == 'EN':
            self.lang_dict[key] = key

    self.ui_rename()
