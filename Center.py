from PyQt5.QtWidgets import QDesktopWidget


def center(self):
    '''
    Centers the window on the screen

    Центрирует окно на экране
    :return:
    '''
    # geometry of the main window
    # размеры главного окна
    qr = self.frameGeometry()
    # center point of screen
    # центр экрана
    cp = QDesktopWidget().availableGeometry().center()
    # move rectangle's center point to screen's center point
    # перемещение прямоугольника в центр экрана
    qr.moveCenter(cp)
    # top left of rectangle becomes top left of window centering it
    # верхний левый угол прямоугольника совмещается с главным окном
    self.move(qr.topLeft())
