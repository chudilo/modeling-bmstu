import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont
from PySide2.QtWidgets import (QFrame, QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QTextEdit, QGridLayout)
from PySide2.QtCharts import QtCharts
import random
from math import fabs
from metods import Data


def func(widget):
    def wrap():
        return widget.update()

    return wrap


# TODO: qt mvc
class RandomNumbersWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.data = Data(1000)

        self.tablesFrames = dict()
        self.tablesRatings = dict()

        self.globalLayout = QGridLayout()
        self.globalLayout.addLayout(self.drawTable("Табличный метод", "tab"), 0, 0)
        self.globalLayout.addLayout(self.drawTable("Алгоритмический метод", "alg"), 0, 1)
        self.globalLayout.addLayout(self.drawHandInput("hand"), 0, 2)

        button = QPushButton("Рассчитать")
        button.clicked.connect(self.buttonCalculateClicked)
        button.setMinimumSize(100, 70)
        buttonLayout = QVBoxLayout()
        buttonLayout.setMargin(20)
        buttonLayout.addWidget(button)

        self.globalLayout.addLayout(buttonLayout, 2, 2)

        self.warningLabel = QLabel("")
        warningLayout = QVBoxLayout()
        warningLayout.addWidget(self.warningLabel)
        self.globalLayout.addLayout(warningLayout, 2, 1)

        button = QPushButton("Сгенерировать\nновые\nпоследовательности")
        button.setMinimumSize(170, 70)
        button.clicked.connect(self.buttonGenerateClicked)
        buttonLayout = QVBoxLayout()
        buttonLayout.setMargin(20)
        buttonLayout.addWidget(button)

        self.globalLayout.addLayout(buttonLayout, 2, 0)
#widg = QLineEdit()7
        #widg.setMaxLength(30)
        #self.globalLayout.addWidget(widg)

        self.globalLayout.setSpacing(50)
        #self.globalLayout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.globalLayout)

    def buttonGenerateClicked(self):
        self.data.refresh()

        for i in range(3):
            for j in range(10):
                self.tablesFrames['alg'][i][j].setText(str(self.data.tables['alg'][i][j]))
                self.tablesFrames['tab'][i][j].setText(str(self.data.tables['tab'][i][j]))
            self.tablesRatings['alg'][i].setText("{:6.5f}".format(self.data.ratings['alg'][i]))
            self.tablesRatings['tab'][i].setText("{:6.5f}".format(self.data.ratings['tab'][i]))

    def buttonCalculateClicked(self):
        self.data.tables['hand'] = []
        try:
            for i in range(10):
                field = self.tablesFrames['hand'][i].text()
                if field:
                    num = int(field)
                    self.data.tables['hand'].append(num)

            self.data.ratings['hand'] = Data.correlation(self.data.tables['hand'])
            self.tablesRatings['hand'].setText("{:6.5f}".format(self.data.ratings['hand']))

            self.warningLabel.setText("")
        except ValueError:
            self.warningLabel.setText("Ошибка:\nНеправильный ввод чисел")
            self.tablesRatings['hand'].setText("%###")
        except Exception as e:
            self.warningLabel.setText(e)
            self.tablesRatings['hand'].setText("%###")

    def drawTable(self, name, dictName):
        self.tablesFrames[dictName] = list()

        layout = QHBoxLayout()
        for _ in range(3):
            row = []
            column = QVBoxLayout()
            for _ in range(10):
                cell = QLabel()
                cell.setMinimumSize(80, 25)
                cell.setFrameShape(QFrame.WinPanel)
                cell.setFrameShadow(QFrame.Raised)
                row.append(cell)
                column.addWidget(cell)

            self.tablesFrames[dictName].append(row)
            layout.addLayout(column)

        layout.setSpacing(1)

        all = QVBoxLayout()
        temp = QVBoxLayout()
        header = QLabel(name)
        header.setAlignment(Qt.AlignBottom)
        temp.addWidget(header)
        temp.setSpacing(0)

        subHeader = QLabel("Оценка\nпослед-тей:")
        subHeader.setMaximumSize(100, 40)

        stat = QHBoxLayout()
        self.tablesRatings[dictName] = []
        for i in range(3):
            p = QLabel("%###")
            p.setFrameShape(QFrame.WinPanel)
            p.setFrameShadow(QFrame.Raised)
            stat.addWidget(p)
            self.tablesRatings[dictName].append(p)

        all.setSpacing(10)
        all.setMargin(20)
        all.addLayout(temp)
        all.addLayout(layout)
        all.addWidget(subHeader)
        all.addLayout(stat)

        return all

    def drawHandInput(self, dictName):
        self.tablesFrames[dictName] = []

        column = QVBoxLayout()
        column.setSpacing(1)
        for _ in range(10):
            cell = QLineEdit()
            cell.setMinimumSize(30, 25)
            cell.setMaximumSize(200, 50)
            column.addWidget(cell)
            self.tablesFrames[dictName].append(cell)

        all = QVBoxLayout()
        temp = QVBoxLayout()
        header = QLabel("Ручной ввод")
        header.setAlignment(Qt.AlignBottom)
        temp.addWidget(header)

        subHeader = QLabel("Оценка\nпослед-тей:")
        subHeader.setMaximumSize(100, 40)

        percent = QLabel("%###")
        percent.setFrameShape(QFrame.WinPanel)
        percent.setFrameShadow(QFrame.Raised)
        self.tablesRatings[dictName] = percent

        all.setSpacing(10)
        all.setMargin(20)
        all.addLayout(temp)
        all.addLayout(column)
        all.addWidget(subHeader)
        all.addWidget(percent)

        return all


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")
        self.resize(800, 600)

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
