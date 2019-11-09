from functools import partial


def buttons_connect(self):
    '''
    Connects buttons to methods

    Подключает кнопки к методам
    :param self:
    :return:
    '''
    # TODO: add button scaling dependant on window size

    self.btnSearch.clicked.connect(self.search)

    self.actionProblems_All.triggered.connect(partial(self.change_section, 'ALL', 'PROBLEM'))
    self.actionStudentsBook_All.triggered.connect(partial(self.change_section, 'ALL', 'BOOK'))
    self.actionLessons_All.triggered.connect(partial(self.change_section, 'ALL', 'LESSON'))
    self.actionIndependentWorks_All.triggered.connect(partial(self.change_section, 'ALL', 'IWORK'))
    self.actionTests_All.triggered.connect(partial(self.change_section, 'ALL', 'TEST'))
    self.actionAll_All.triggered.connect(partial(self.change_section, 'ALL', 'ALL'))

    self.actionProblems_FY.triggered.connect(partial(self.change_section, 'FY', 'PROBLEM'))
    self.actionStudentsBook_FY.triggered.connect(partial(self.change_section, 'FY', 'BOOK'))
    self.actionLessons_FY.triggered.connect(partial(self.change_section, 'FY', 'LESSON'))
    self.actionIndependentWorks_FY.triggered.connect(partial(self.change_section, 'FY', 'IWORK'))
    self.actionTests_FY.triggered.connect(partial(self.change_section, 'FY', 'TEST'))
    self.actionAll_FY.triggered.connect(partial(self.change_section, 'FY', 'ALL'))

    self.actionProblems_SY.triggered.connect(partial(self.change_section, 'SY', 'PROBLEM'))
    self.actionStudentsBook_SY.triggered.connect(partial(self.change_section, 'SY', 'BOOK'))
    self.actionLessons_SY.triggered.connect(partial(self.change_section, 'SY', 'LESSON'))
    self.actionAll_SY.triggered.connect(partial(self.change_section, 'SY', 'ALL'))

    self.actionOpenTutorial.triggered.connect(self.open_tutorial)

    self.actionOpenFullDB.triggered.connect(self.open_full_db)

    self.actionOpenDBUpdater.triggered.connect(self.open_db_updater)

    self.actionResetAll.triggered.connect(self.reset_all)

    self.actionRussian.triggered.connect(partial(self.change_language, 'RU'))
    self.actionEnglish.triggered.connect(partial(self.change_language, 'EN'))
