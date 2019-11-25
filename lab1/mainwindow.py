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
        #print(text)
        return widget.update()

    return wrap

# TODO: qt mvc
# FIXME: trying

class Data(object):
    def __init__(self):
        '''
        arrTabel1 = []
        arrTabel2 = []
        arrTabel3 = []

        algTabel1 = []
        algTabel2 = []
        algTabel3 = []

        handTabel = []
        results = []
        '''
        #self.alg_table_fill()

    def refresh(self):
        self.alg_table_fill()

    def alg_table_fill(self):
        random.seed()
        self.one_digit_alg = [random.randint(0, 9) for i in range(10)]
        self.two_digits_alg = [random.randint(10, 99) for i in range(10)]
        self.three_digits_alg = [random.randint(100, 999) for i in range(10)]

        #table.resizeColumnsToContents()
        self.corel_1 = fabs(self.corelation(self.one_digit_alg))
        self.corel_2 = fabs(self.corelation(self.two_digits_alg))
        self.corel_3 = fabs(self.corelation(self.three_digits_alg))


    def corelation(self, nums):
        n = len(nums)
        sumUU = 0
        sumber = sum(nums)
        sumU2 = 0
        if n ==0:
            return 0
        for i in range(n):
            numj = int(nums[(i+1) % n])
            numi = int(nums[i])
            sumU2 += numi * numi
            sumUU += numi * numj
        top = n * sumUU - sumber ** 2
        bottom = n * sumU2 - sumber ** 2
        if bottom == 0:
            return 1

        return top / bottom


class Widget(QWidget):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Widget()

    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec_())
