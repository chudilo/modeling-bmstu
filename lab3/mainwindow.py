from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont, QIcon
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton,
                               QLineEdit, QTabWidget, QLabel, QFormLayout,
                               QAction, QTableWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QStyledItemDelegate)

import pyqtgraph as pg
import numpy as np
from math import e, pi, sqrt, erf


def gaussDens(x, m=0, d=1):
    return e**(-(x - m)**2/(2 * d**2))/(d * sqrt(2*pi))


def gaussDist(x, m=0, d=1):
    return 1/2*(1 + erf((x - m)/sqrt(2*d**2)))


def uniformDens(x, a, b):
    if a < x <= b:
        return 1/(b-a)
    else:
        return 0


def uniformDist(x, a, b):
    if x <= a:
        return 0
    elif x > b:
        return 1
    else:
        return (x-a)/(b-a)



class WdgPlot(QWidget):
    def __init__(self, parent=None):
        super(WdgPlot, self).__init__(parent)
        layout = QVBoxLayout(self)

        pw = pg.PlotWidget()
        layout.addWidget(pw)
        self.setLayout(layout)

class UniformGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.inputA = QLineEdit("0")
        self.inputB = QLineEdit("10")
        self.inputA.setMinimumSize(30, 25)
        self.inputA.setMaximumSize(150, 50)
        self.inputB.setMinimumSize(30, 25)
        self.inputB.setMaximumSize(150, 50)
        self.layout.addRow(QLabel("a :"), self.inputA)
        self.layout.addRow(QLabel("b :"), self.inputB)
        self.layout.setSpacing(10)

        self.hLayout = QHBoxLayout()
        self.hLayout.addLayout(self.layout)
        self.b = QPushButton("Plot")
        self.b.setMinimumSize(100, 50)
        self.b.clicked.connect(self.plot)

        self.warningLabel = QLabel("")
        self.hLayout.addWidget(self.warningLabel)
        self.hLayout.addWidget(self.b)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.hLayout)
        self.gLayout = QHBoxLayout()
        #self.graphDens = pg.PlotWidget()#WdgPlot()
        #self.graphDist = pg.PlotWidget()
        g1 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        g2 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.graphDist = g2.addPlot()
        self.graphDens = g1.addPlot()
        self.graphDist.showGrid(x=True, y=True)
        self.graphDens.showGrid(x=True, y=True)
        self.gLayout.addWidget(g1)
        self.gLayout.addWidget(g2)
        self.mainLayout.addLayout(self.gLayout)
        self.setLayout(self.mainLayout)

    def plot(self):
        try:
            a = float(self.inputA.text())
            b = float(self.inputB.text())
        except Exception as e:
            self.warningLabel.setText("Incorrect input")
            return

        self.warningLabel.setText("")

        if a > b:
            a, b = b, a
        left_border = a - (b-a)*0.4
        right_border = b + (b-a)*0.4

        steps = 1000
        step = (right_border - left_border) / steps
        X = []
        Y = []
        Y0 = []
        Y1 = []

        while left_border < right_border:
            X.append(left_border)
            Y.append(uniformDens(left_border, a, b))
            Y0.append(0)
            Y1.append(uniformDist(left_border, a, b))
            left_border += step

        self.graphDens.clear()
        self.graphDist.clear()

        print(X, Y)
        self.graphDens.plot(X, Y, pen='r')
        self.graphDist.plot(X, Y1, pen='b')


class GaussGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.inputA = QLineEdit("0")
        self.inputB = QLineEdit("1")
        self.inputA.setMinimumSize(30, 25)
        self.inputA.setMaximumSize(150, 50)
        self.inputB.setMinimumSize(30, 25)
        self.inputB.setMaximumSize(150, 50)
        self.layout.addRow(QLabel("\u03BC :"), self.inputA)
        self.layout.addRow(QLabel("\u03C3 :"), self.inputB)
        self.layout.setSpacing(10)

        self.hLayout = QHBoxLayout()
        self.hLayout.addLayout(self.layout)
        self.b = QPushButton("Plot")
        self.b.setMinimumSize(100, 50)
        self.b.clicked.connect(self.plot)

        self.warningLabel = QLabel("")
        self.hLayout.addWidget(self.warningLabel)
        self.hLayout.addWidget(self.b)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.hLayout)
        self.gLayout = QHBoxLayout()
        #self.graphDens = pg.PlotWidget()#WdgPlot()
        #self.graphDist = pg.PlotWidget()
        g1 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        g2 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.graphDist = g2.addPlot()
        self.graphDens = g1.addPlot()
        self.graphDist.showGrid(x=True, y=True)
        self.graphDens.showGrid(x=True, y=True)
        self.gLayout.addWidget(g1)
        self.gLayout.addWidget(g2)
        self.mainLayout.addLayout(self.gLayout)
        self.setLayout(self.mainLayout)

    def plot(self):
        try:
            m = float(self.inputA.text())
            d = float(self.inputB.text())
        except Exception as e:
            self.warningLabel.setText("Incorrect input")
            return

        self.warningLabel.setText("")

        if d <= 0:
            self.warningLabel.setText("Incorrect input")
            return

        left_border = m - d*5
        right_border = m + d*5

        steps = 2000
        step = (right_border - left_border) / steps
        X = []
        Y = []
        Y0 = []
        Y1 = []

        while left_border < right_border:
            X.append(left_border)
            Y.append(gaussDens(left_border, m, d))
            Y0.append(0)
            Y1.append(gaussDist(left_border, m, d))
            left_border += step

        self.graphDens.clear()
        self.graphDist.clear()

        print(X, Y)
        # X = [1,2,3,4,5]
        # Y = [1,2,3,4,5]
        self.graphDens.plot(X, Y, pen='r')
        self.graphDist.plot(X, Y1, pen='b')


class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.mainLayout.addWidget(QLabel("Distribution:"))
        self.mainLayout.addWidget(self.tabs)

        self.tabs.addTab(UniformGraph(), "Uniform")
        self.tabs.addTab(GaussGraph(), "Gauss")
        self.setLayout(self.mainLayout)


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")
        self.resize(1000, 500)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        newFont = QFont("Arial", 12)
        widget.setFont(newFont)
        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()
