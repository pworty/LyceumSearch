from functools import partial


def buttonsConnect(self):
    '''
    Connects buttons to methods

    Подключает кнопки к методам
    :param self:
    :return:
    '''
    # TODO: add button scaling dependant on window size

    self.btnSearch.clicked.connect(self.search)

    self.actionProblems_All.triggered.connect(partial(self.changeSection, 'ALL', 'PROBLEM'))
    self.actionStudentsBook_All.triggered.connect(partial(self.changeSection, 'ALL', 'BOOK'))
    self.actionLessons_All.triggered.connect(partial(self.changeSection, 'ALL', 'LESSON'))
    self.actionIndependentWorks_All.triggered.connect(partial(self.changeSection, 'ALL', 'IWORK'))
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
