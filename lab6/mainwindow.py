from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont, QIcon
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QFrame, QBoxLayout,
                               QAction, QTableWidget, QFormLayout, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QStyledItemDelegate)

import math
import random
from copy import deepcopy


class IconDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        option.decorationSize = option.rect.size()


class ServingMachineStatistics(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        self.shopLayout = QHBoxLayout()

        self.visitorLabel = QLabel("Visitor")
        self.mVisitorLabel = QLabel("\u03BC")
        self.mVisitorLine = QLineEdit("0.5")
        self.sigmaVisitorLabel = QLabel("\u03C3")
        self.sigmaVisitorLine = QLineEdit("0.2")
        self.visitorBox = QFormLayout()
        self.visitorBox.addWidget(self.visitorLabel)
        self.visitorBox.addRow(self.mVisitorLabel, self.mVisitorLine)
        self.visitorBox.addRow(self.sigmaVisitorLabel, self.sigmaVisitorLine)
        self.visitorBox.setSpacing(5)

        self.vendorLabel = QLabel("Vendor")
        self.mVendorLabel = QLabel("\u03BC")
        self.mVendorLine = QLineEdit("0.6")
        self.sigmaVendorLabel = QLabel("\u03C3")
        self.sigmaVendorLine = QLineEdit("0.3")
        self.vendorBox = QFormLayout()
        self.vendorBox.addWidget(self.vendorLabel)
        self.vendorBox.addRow(self.mVendorLabel, self.mVendorLine)
        self.vendorBox.addRow(self.sigmaVendorLabel, self.sigmaVendorLine)
        self.vendorBox.setSpacing(5)

        self.tableLayout = QHBoxLayout()
        self.closeTableLayout = QVBoxLayout()
        self.farTableLayout = QVBoxLayout()

        self.closeTableLayout.addWidget(QLabel("Close tables for candles"))
        self.visitorLabel = QLabel("Table1")
        self.mLabelt1 = QLabel("Size")
        self.mLinet1 = QLineEdit("15")
        self.sigmaLabelt1 = QLabel("T of cleaning")
        self.sigmaLinet1 = QLineEdit("20")
        self.tableBox1 = QFormLayout()
        self.tableBox1.addWidget(self.visitorLabel)
        self.tableBox1.addRow(self.mLabelt1, self.mLinet1)
        self.tableBox1.addRow(self.sigmaLabelt1, self.sigmaLinet1)
        self.tableBox1.setSpacing(5)

        self.vendorLabel = QLabel("Table2")
        self.mLabelt2 = QLabel("Size")
        self.mLinet2 = QLineEdit("15")
        self.sigmaLabelt2 = QLabel("T of cleaning")
        self.sigmaLinet2 = QLineEdit("25")
        self.tableBox2 = QFormLayout()
        self.tableBox2.addWidget(self.vendorLabel)
        self.tableBox2.addRow(self.mLabelt2, self.mLinet2)
        self.tableBox2.addRow(self.sigmaLabelt2, self.sigmaLinet2)
        self.tableBox2.setSpacing(5)

        self.closeTableLayout.addLayout(self.tableBox1)
        self.closeTableLayout.addLayout(self.tableBox2)

        self.visitorLabel = QLabel("Table3")
        self.mLabelt3 = QLabel("Size")
        self.mLinet3 = QLineEdit("5")
        self.sigmaLabelt3 = QLabel("T of cleaning")
        self.sigmaLinet3 = QLineEdit("25")
        self.tableBox3 = QFormLayout()
        self.tableBox3.addWidget(self.visitorLabel)
        self.tableBox3.addRow(self.mLabelt3, self.mLinet3)
        self.tableBox3.addRow(self.sigmaLabelt3, self.sigmaLinet3)
        self.tableBox3.setSpacing(5)

        self.vendorLabel = QLabel("Table4")
        self.mLabelt4 = QLabel("Size")
        self.mLinet4 = QLineEdit("5")
        self.sigmaLabelt4 = QLabel("T of cleaning")
        self.sigmaLinet4 = QLineEdit("30")
        self.tableBox4 = QFormLayout()
        self.tableBox4.addWidget(self.vendorLabel)
        self.tableBox4.addRow(self.mLabelt4, self.mLinet4)
        self.tableBox4.addRow(self.sigmaLabelt4, self.sigmaLinet4)
        self.tableBox4.setSpacing(5)

        self.farTableLayout.addWidget(QLabel("Far tables for candles"))
        self.farTableLayout.addLayout(self.tableBox3)
        self.farTableLayout.addLayout(self.tableBox4)

        self.closeTableLayout.setSpacing(5)
        self.farTableLayout.setSpacing(5)
        self.tableLayout.addLayout(self.closeTableLayout)
        self.tableLayout.addLayout(self.farTableLayout)

        self.shopLayout.addLayout(self.visitorBox)
        self.shopLayout.addLayout(self.vendorBox)

        self.answerLayout = QHBoxLayout()

        self.answerLabel = QLabel("")
        self.numLabel = QLabel("Number of requests")
        self.numLine = QLineEdit("5000")
        self.failLabel = QLabel("Queue fails")
        self.failLine = QLabel("")
        self.failLine.setFrameShape(QFrame.WinPanel)
        self.failLine.setFrameShadow(QFrame.Raised)
        self.fail2Label = QLabel("Busy tables fails")
        self.fail2Line = QLabel("")
        self.fail2Line.setFrameShape(QFrame.WinPanel)
        self.fail2Line.setFrameShadow(QFrame.Raised)
        self.probLabel = QLabel("Probability of failing")
        self.probLine = QLabel("")
        self.probLine.setFrameShape(QFrame.WinPanel)
        self.probLine.setFrameShadow(QFrame.Raised)
        self.answerBox = QFormLayout()
        self.answerBox.addWidget(self.answerLabel)
        self.answerBox.addRow(self.numLabel, self.numLine)
        self.answerBox.addRow(self.failLabel, self.failLine)
        self.answerBox.addRow(self.fail2Label, self.fail2Line)
        self.answerBox.addRow(self.probLabel, self.probLine)

        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate)
        self.button.setMinimumSize(150, 65)
        self.button.setMaximumSize(250, 65)
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.button)
        self.buttonLayout.setAlignment(Qt.AlignHCenter)

        self.answerLayout.addLayout(self.answerBox)
        self.answerLayout.addLayout(self.buttonLayout)
        self.answerLayout.setSpacing(5)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addLayout(self.shopLayout)
        self.mainLayout.addLayout(self.tableLayout)
        self.mainLayout.addWidget(line)
        self.mainLayout.addLayout(self.answerLayout)
        self.mainLayout.setSpacing(40)
        self.setLayout(self.mainLayout)

    def calculate(self):
        mVisitor = float(self.mVisitorLine.text())
        sigmVisitor = float(self.sigmaVisitorLine.text())

        mVendor = float(self.mVendorLine.text())
        sigmVendor = float(self.sigmaVendorLine.text())

        mt1 = float(self.mLinet1.text())
        st1 = float(self.sigmaLinet1.text())

        mt2 = float(self.mLinet2.text())
        st2 = float(self.sigmaLinet2.text())

        mt3 = float(self.mLinet3.text())
        st3 = float(self.sigmaLinet3.text())

        mt4 = float(self.mLinet4.text())
        st4 = float(self.sigmaLinet4.text())

        n = int(self.numLine.text())

        queueFailed, tableFailed = runModel(n, Generator(mVisitor, sigmVisitor), Generator(mVendor, sigmVendor),
                                  Table(mt1, st1), Table(mt2, st2), Table(mt3, st3), Table(mt4, st4))

        self.failLine.setText(str(queueFailed))
        self.fail2Line.setText(str(tableFailed))
        self.probLine.setText("{:.4}".format((queueFailed + tableFailed)/n))


def getCurrentEvent(visitorT, vendorT, closeTables, farTables):
    minTime = visitorT
    eventType = "visitor"
    index = None
    if vendorT:
        if vendorT[0] < minTime:
            minTime = visitorT
            eventType = "vendor"

    for i in range(len(closeTables)):
        if closeTables[i] is not None:
            if closeTables[i] < minTime:
                minTime = closeTables[i]
                eventType = "close table"
                index = i

    for i in range(len(farTables)):
        if farTables[i]:
            if farTables[i] < minTime:
                minTime = farTables[i]
                eventType = "far table"
                index = i

    return eventType, index


class Table(object):
    def __init__(self, size, const):
        self.fullness = 0
        self.maxSize = size
        self.t = const

    def getWorkTime(self):
        return self.t

    def push(self):
        if self.fullness < self.maxSize:
            self.fullness += 1
            return True
        else:
            return False

    def clear(self):
        self.fullness = 0


def runModel(n, visitor, vendor, table1, table2, table3, table4):
    visitorT = visitor.getWorkTime()
    vendorT = []
    closeTables = [table1.getWorkTime(), table2.getWorkTime()]
    farTables = [table3.getWorkTime(), table4.getWorkTime()]

    queueFailed = 0
    tableFailed = 0
    requestsCount = 0
    peopleCount = 1

    while peopleCount < n:
        eventType, index = getCurrentEvent(visitorT, vendorT, closeTables, farTables)
        #print(visitorT, vendorT)
        #print(closeTables, farTables)

        if eventType == "visitor":
            if random.random() > 1/(1 + len(vendorT)*0.2):
                queueFailed += 1
            else:
                if vendorT:
                    vendorT.append(vendorT[-1] + vendor.getWorkTime())
                else:
                    vendorT.append(visitorT + vendor.getWorkTime())

            visitorT += visitor.getWorkTime()
            peopleCount += 1

        elif eventType == "vendor":
            if table1.push():
                requestsCount += 1

            elif table2.push():
                requestsCount += 1
            else:
                if random.random() < 0.5:
                    tableFailed += 1
                elif table3.push():
                    requestsCount += 1
                elif table4.push():
                    requestsCount += 1
                else:
                    tableFailed += 1

            vendorT.pop(0)

        elif eventType == "close table":
            if index == 0:
                table1.clear()
                closeTables[0] += table1.getWorkTime()
            else:
                table2.clear()
                closeTables[1] += table2.getWorkTime()

        elif eventType == "far table":
            if index == 0:
                table3.clear()
                farTables[0] += table3.getWorkTime()
            else:
                table4.clear()
                farTables[1] += table4.getWorkTime()

    print(queueFailed, tableFailed)
    return queueFailed, tableFailed


class Generator(object):
    def __init__(self, m, sigma):
        self.__m = m
        self.__sigma = sigma

    def getWorkTime(self):
        res = self.__m + (random.random() - 0.5) * 2 * self.__sigma
        return res


print(runModel(500, Generator(0.5, 0.2), Generator(0.5, 0.1),
               Table(30, 20), Table(30, 25), Table(10, 30), Table(10, 30)))

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
