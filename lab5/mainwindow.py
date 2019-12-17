from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont, QIcon
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QFrame, QBoxLayout,
                               QAction, QTableWidget, QFormLayout, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QStyledItemDelegate)

import math
import random
import numpy
from copy import deepcopy


class IconDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        option.decorationSize = option.rect.size()


class ServingMachineStatistics(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.generatorLabel = QLabel("Generator")
        self.mLabel = QLabel("\u03BC")
        self.mLine = QLineEdit("10")
        self.sigmaLabel = QLabel("\u03C3")
        self.sigmaLine = QLineEdit("2")
        self.genBox = QFormLayout()
        self.genBox.addWidget(self.generatorLabel)
        self.genBox.addRow(self.mLabel, self.mLine)
        self.genBox.addRow(self.sigmaLabel, self.sigmaLine)
        self.genBox.setSpacing(5)

        self.operatorLayout = QHBoxLayout()

        self.operatorLabel1 = QLabel("Operator 1")
        self.mLabel1 = QLabel("\u03BC")
        self.mLine1 = QLineEdit("20")
        self.sigmaLabel1 = QLabel("\u03C3")
        self.sigmaLine1 = QLineEdit("5")
        self.operatorBox1 = QFormLayout()
        self.operatorBox1.addWidget(self.operatorLabel1)
        self.operatorBox1.addRow(self.mLabel1, self.mLine1)
        self.operatorBox1.addRow(self.sigmaLabel1, self.sigmaLine1)
        self.operatorBox1.setSpacing(5)

        self.operatorLabel2 = QLabel("Operator 2")
        self.mLabel2 = QLabel("\u03BC")
        self.mLine2 = QLineEdit("40")
        self.sigmaLabel2 = QLabel("\u03C3")
        self.sigmaLine2 = QLineEdit("10")
        self.operatorBox2 = QFormLayout()
        self.operatorBox2.addWidget(self.operatorLabel2)
        self.operatorBox2.addRow(self.mLabel2, self.mLine2)
        self.operatorBox2.addRow(self.sigmaLabel2, self.sigmaLine2)
        self.operatorBox2.setSpacing(5)

        self.operatorLabel3 = QLabel("Operator 3")
        self.mLabel3 = QLabel("\u03BC")
        self.mLine3 = QLineEdit("40")
        self.sigmaLabel3 = QLabel("\u03C3")
        self.sigmaLine3 = QLineEdit("20")
        self.operatorBox3 = QFormLayout()
        self.operatorBox3.addWidget(self.operatorLabel3)
        self.operatorBox3.addRow(self.mLabel3, self.mLine3)
        self.operatorBox3.addRow(self.sigmaLabel3, self.sigmaLine3)
        self.operatorBox3.setSpacing(5)

        self.operatorLayout.addLayout(self.operatorBox1)
        self.operatorLayout.addLayout(self.operatorBox2)
        self.operatorLayout.addLayout(self.operatorBox3)
        self.operatorLayout.setSpacing(40)

        self.computerLayout = QHBoxLayout()

        self.computerLabel1 = QLabel("Computer 1")
        self.tLabel1 = QLabel("const")
        self.tLine1 = QLineEdit("15")
        self.computerBox1 = QFormLayout()
        self.computerBox1.addWidget(self.computerLabel1)
        self.computerBox1.addRow(self.tLabel1, self.tLine1)
        self.computerBox1.setSpacing(5)

        self.computerLabel2 = QLabel("Computer 2")
        self.tLabel2 = QLabel("const")
        self.tLine2 = QLineEdit("30")
        self.computerBox2 = QFormLayout()
        self.computerBox2.addWidget(self.computerLabel2)
        self.computerBox2.addRow(self.tLabel2, self.tLine2)
        self.computerBox2.setSpacing(5)

        self.computerLayout.addLayout(self.computerBox1)
        self.computerLayout.addLayout(self.computerBox2)
        self.computerLayout.setSpacing(40)

        self.answerLayout = QHBoxLayout()

        self.answerLabel = QLabel("")
        self.numLabel = QLabel("Number of requests")
        self.numLine = QLineEdit("300")
        self.failLabel = QLabel("Failed requests")
        self.failLine = QLabel("61")
        self.failLine.setFrameShape(QFrame.WinPanel)
        self.failLine.setFrameShadow(QFrame.Raised)
        self.probLabel = QLabel("Probability of failing")
        self.probLine = QLabel("0.2033")
        self.probLine.setFrameShape(QFrame.WinPanel)
        self.probLine.setFrameShadow(QFrame.Raised)
        self.answerBox = QFormLayout()
        self.answerBox.addWidget(self.answerLabel)
        self.answerBox.addRow(self.numLabel, self.numLine)
        self.answerBox.addRow(self.failLabel, self.failLine)
        self.answerBox.addRow(self.probLabel, self.probLine)

        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate)
        self.button.setMinimumSize(150,65)
        self.button.setMaximumSize(250, 65)
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.button)
        self.buttonLayout.setAlignment(Qt.AlignVCenter)

        self.answerLayout.addLayout(self.answerBox)
        self.answerLayout.addLayout(self.buttonLayout)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addLayout(self.genBox)
        self.mainLayout.addLayout(self.operatorLayout)
        self.mainLayout.addLayout(self.computerLayout)
        self.mainLayout.addWidget(line)
        self.mainLayout.addLayout(self.answerLayout)

        self.setLayout(self.mainLayout)

    def calculate(self):
        mGen = float(self.mLine.text())
        sigmGen = float(self.sigmaLine.text())

        mOper1 = float(self.mLine1.text())
        sigmOper1 = float(self.sigmaLine1.text())
        mOper2 = float(self.mLine2.text())
        sigmOper2 = float(self.sigmaLine2.text())
        mOper3 = float(self.mLine3.text())
        sigmOper3 = float(self.sigmaLine3.text())

        tComp1 = float(self.tLine1.text())
        tComp2 = float(self.tLine2.text())

        n = int(self.numLine.text())

        #print(mGen, sigmGen)
        #print(mOper1, sigmOper1)
        #print(mOper2, sigmOper2)
        #print(mOper3, sigmOper3)
        #print(tComp1, tComp2, n)

        requestsFailed = runModel(n, Generator(mGen, sigmGen), Generator(mOper1, sigmOper1),
                 Generator(mOper2, sigmOper2), Generator(mOper3, sigmOper3),
                 Computer(tComp1), Computer(tComp2))

        self.failLine.setText(str(requestsFailed))
        self.probLine.setText("{:.4}".format(requestsFailed/(n)))


def runModel(n, gen, op0, op1, op2, comp0, comp1):
    generator = gen.getWorkTime()
    operators = [None, None, None]
    computers = [[None], [None]]

    requestsFailed = 0
    requestsCount = 1
    peopleCount = 1

    while peopleCount < n:
        m = generator
        event = 0
        for i in range(len(operators)):
            if operators[i] is not None:
                if operators[i] < m:
                    m = operators[i]
                    index = i
                    event = 1

        for i in range(len(computers)):
            if computers[i][0] is not None:
                if min(computers[i]) < m:
                    m = computers[i][0]
                    index = i
                    event = 2

        if event == 0:
            if operators[0] is None:
                operators[0] = generator + op0.getWorkTime()
            elif operators[1] is None:
                operators[1] = generator + op1.getWorkTime()
            elif operators[2] is None:
                operators[2] = generator + op2.getWorkTime()
            else:
                requestsFailed += 1

            generator += gen.getWorkTime()
            peopleCount += 1

        elif event == 1:
            if index == 2:
                if computers[1][-1] is None:
                    computers[1] = []
                    computers[1].append(operators[index] + comp1.getWorkTime())

            else:
                if computers[0][-1] is None:
                    computers[0] = []
                    computers[0].append(operators[index] + comp0.getWorkTime())

            operators[index] = None

        elif event == 2:
            computers[index].pop(0)
            if not computers[index]:
                computers[index] = [None]

            requestsCount += 1

    return requestsFailed


class Generator(object):
    def __init__(self, m, sigma):
        self.__m = m
        self.__sigma = sigma

    def getWorkTime(self):
        res = self.__m + (random.random() - 0.5) * 2 * self.__sigma
        return res


class Computer(object):
    def __init__(self, t):
        self.__t = t

    def getWorkTime(self):
        return self.__t


class RequestQueue(object):
    def __init__(self):
        self.l = 0
        self.max = 0

    def dec(self):
        if self.l > 0:
            self.l -= 1
            return True
        else:
            return False

    def inc(self):
        self.l += 1
        if self.max < self.l:
            self.max = self.l


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Система массового обслуживанияи")
        self.resize(800, 600)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()
