import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import (QFrame, QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QTextEdit, QGridLayout)
from PySide2.QtCharts import QtCharts
import random
from math import fabs


def asd(qwe):
    pass


def func(widget):
    def wrap():
        return widget.update()

    return wrap


# TODO: qt mvc
# TODO: fillTablesTab function
class Data(object):
    def __init__(self):
        self.__initDataFields()

    def __initDataFields(self):
        self.tables = dict()
        self.tables['tab'] = [[], [], []]
        self.tables['alg'] = [[], [], []]
        self.tables['hand'] = []

        self.ratings = dict()
        self.ratings['tab'] = None
        self.ratings['alg'] = None
        self.ratings['hand'] = None

    def fillTablesAlg(self, num):
        self.tables['alg'][0] = self.getTableAlg(num, 0, 9)
        self.tables['alg'][1] = self.getTableAlg(num, 10, 99)
        self.tables['alg'][2] = self.getTableAlg(num, 100, 999)

        self.ratings['alg'][0] = self.getRating(self.tables['alg'][0])
        self.ratings['alg'][1] = self.getRating(self.tables['alg'][1])
        self.ratings['alg'][2] = self.getRating(self.tables['alg'][2])

    @staticmethod
    def getTableAlg(num, leftBord, rightBord):
        arr = [random.randint(leftBord, rightBord) for _ in range(num)]
        return arr

    @staticmethod
    def getRating(array):
        # TODO: This is stub, place for a function that evaluates the sequence
        return array


class RandomNumbersWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.arr = []
        self.data = Data()
        self.globalLayout = QGridLayout()
        self.globalLayout.addLayout(self.drawTable("Табличный метод"), 0, 0)
        #self.globalLayout.addLayout(self.drawTable("Алгоритмический метод"), 0, 1)
        self.globalLayout.addLayout(self.drawColumn(), 0 , 2)

        button = QPushButton("Рассчитать")
        button.clicked.connect(self.buttonClicked)
        button.setMinimumSize(100,70)
        buttonLayout = QVBoxLayout()
        buttonLayout.setMargin(30)
        buttonLayout.addWidget(button)

        self.globalLayout.addLayout(buttonLayout, 1, 2)

        button = QPushButton("Сгенерировать\nновые\nпоследовательности")
        button.setMinimumSize(100,70)
        button.clicked.connect(self.buttonClicked)
        buttonLayout = QVBoxLayout()
        buttonLayout.setMargin(30)
        buttonLayout.addWidget(button)

        self.globalLayout.addLayout(buttonLayout, 1, 0)
#widg = QLineEdit()7
        #widg.setMaxLength(30)
        #self.globalLayout.addWidget(widg)

        self.globalLayout.setSpacing(50)
        #self.globalLayout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.globalLayout)

    def buttonClicked(self):
            self.data.refresh()
            for j in range(10):
                self.arr[j].setText(str(self.data.one_digit_alg[j]))
                self.arr[10 + j].setText(str(self.data.two_digits_alg[j]))
                self.arr[20 + j].setText(str(self.data.three_digits_alg[j]))

            self.percent[0].setText(str(self.data.corel_1))
            self.percent[1].setText(str(self.data.corel_2))
            self.percent[2].setText(str(self.data.corel_3))

    def drawTable(self, name, arr=None):
        if arr == None:
            arr = str(random.randint(0,9))

        self.left = QVBoxLayout()
        for i in range(10):
            l = QLabel()
            l.setMinimumSize(20,25)
            l.setFrameShape(QFrame.WinPanel)
            l.setFrameShadow(QFrame.Raised)
            self.arr.append(l)
            self.left.addWidget(l)

        self.mid = QVBoxLayout()
        for i in range(10):
            l = QLabel()
            l.setMinimumSize(20,25)
            l.setFrameShape(QFrame.WinPanel)
            l.setFrameShadow(QFrame.Raised)
            self.arr.append(l)
            self.mid.addWidget(l)

        self.right = QVBoxLayout()
        for i in range(10):
            l = QLabel()
            l.setMinimumSize(20,25)
            l.setFrameShape(QFrame.WinPanel)
            l.setFrameShadow(QFrame.Raised)
            self.arr.append(l)
            self.right.addWidget(l)

        self.layout = QHBoxLayout()
        self.layout.setSpacing(1)
        self.layout.addLayout(self.left)
        self.layout.addLayout(self.mid)
        self.layout.addLayout(self.right)

        all = QVBoxLayout()
        temp = QVBoxLayout()
        l = QLabel(name)
        l.setAlignment(Qt.AlignBottom)
        temp.addWidget(l)
        temp.setSpacing(0)

        stat = QHBoxLayout()
        #stat.setMargin(15)
        self.percent = []
        for i in range(3):
            p = QLabel("%###")
            p.setFrameShape(QFrame.WinPanel)
            p.setFrameShadow(QFrame.Raised)
            stat.addWidget(p)
            self.percent.append(p)

        all.setSpacing(10)
        all.setMargin(30)
        all.addLayout(temp)
        all.addLayout(self.layout)
        all.addLayout(stat)
        #all.setAlignment(Qt.AlignTop)

        return all
        #self.setLayout(self.layout1)

    def drawColumn(self):
        self.left = QVBoxLayout()
        for i in range(10):
            l = QLineEdit()
            #l.setGeometry(40,20)
            l.setMinimumSize(50,25)
            l.setMaximumSize(200,50)
            self.left.addWidget(l)

        self.left.setSpacing(1)
        all = QVBoxLayout()
        temp = QVBoxLayout()
        l = QLabel("Ручной ввод")
        l.setAlignment(Qt.AlignBottom)
        temp.addWidget(l)
        #temp.setSpacing(1)


        #stat.setMargin(15)

        percent = QLabel("%###")
        percent.setFrameShape(QFrame.WinPanel)
        percent.setFrameShadow(QFrame.Raised)
        #stat.addWidget(percent)
        all.setSpacing(5)
        all.setMargin(30)
        all.addLayout(temp)
        all.addLayout(self.left)
        all.addWidget(percent)
        #all.setAlignment(Qt.AlignTop)

        return all


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        newfont = QFont("Arial", 12)
        widget.setFont(newfont)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()
