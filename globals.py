def globals_init(self):
    '''
    Variables init

    Инициализация переменных
    :param self:
    :return:
    '''
    with open("settings.txt", "r") as f:
        data = f.readlines()
    self.SHOW_TUTORIAL, self.DB_NAME, self.LANGUAGE = [d.split(' = ')[1].split('\n')[0] for d in
                                                       data]
    self.SHOW_TUTORIAL = int(self.SHOW_TUTORIAL)
    self.SECTION = 'ALL'
    self.TYPE = 'ALL'
