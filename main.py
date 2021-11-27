import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)  # Загружаем дизайн
        self.flag = False
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            r = 255
            g = 255
            b = 0
            #r = randint(0, 255)
            #g = randint(0, 255)
            #b = randint(0, 255)
            self.color = QColor(r, g, b)
            self.qp.setBrush(self.color)
            self.draw()
            self.qp.end()

    def draw(self):
        size = 100
        x, y = 100, 100
        self.qp.drawEllipse(x - size // 2, y - size // 2, size, size)
        self.drawf()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
