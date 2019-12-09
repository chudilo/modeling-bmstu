from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont, QIcon
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLineEdit,
                               QAction, QTableWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QStyledItemDelegate)

import pyqtgraph as pg
import random
import numpy


class IconDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        option.decorationSize = option.rect.size()


class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        size = 5
        self.table = QTableWidget(size, size)
        self.table.setMaximumSize(275, 295)
        self.table.setHorizontalHeaderLabels([str(i + 1) + "\n " for i in range(size)])

        self.tableResults = QTableWidget(size, 2)
        self.tableResults.horizontalHeader().setDefaultSectionSize(100)
        self.tableResults.verticalHeader().setDefaultSectionSize(50)
        self.tableResults.setMaximumSize(225, 295)
        self.tableResults.setHorizontalHeaderLabels(["Предельные\nвероятности", "Время\nстабилизации"])

        #self.table.setCellWidget(1000, 1000, self)
        self.table.horizontalHeader().setDefaultSectionSize(50)
        self.table.verticalHeader().setDefaultSectionSize(50)
        #self.table.setCellWidget(200, 200, self.table)
        delegate = IconDelegate(self.table)
        self.table.setItemDelegate(delegate)
        self.tableLayout = QHBoxLayout()
        self.tableLayout.addWidget(self.tableResults)
        tmp = QHBoxLayout()
        tmp.addWidget(self.table)
        tmp.setMargin(10)

        self.tableLayout.addLayout(tmp)
        self.tableLayout.setAlignment(Qt.AlignRight)

        self.panel = QVBoxLayout()

        self.cell = QLineEdit()
        self.cell.setMaximumSize(150, 20)

        self.buttonSize = QPushButton("Задать размер")
        self.buttonSize.setMaximumSize(150, 50)
        self.buttonSize.clicked.connect(self.resizeTable)

        self.buttonCalculate = QPushButton("Вычислить")
        self.buttonCalculate.clicked.connect(self.solve)
        self.buttonCalculate.setMaximumSize(150, 50)

        self.panel.addWidget(self.cell)
        self.panel.addWidget(self.buttonSize)
        self.panel.addWidget(self.buttonCalculate)
        self.panel.setAlignment(Qt.AlignTop)

        self.layout.addLayout(self.panel)
        self.layout.addLayout(self.tableLayout)
        self.layout.setAlignment(Qt.AlignTop)
        #self.layout.setAlignment(Qt.AlignRight)

        self.setLayout(self.layout)


    def resizeTable(self):
        print("fill")
        try:
            size = int(self.cell.text())
        except ValueError:
            print("Wrong value")
            return

        print("resize")
        self.table.setColumnCount(size)
        self.table.setRowCount(size)

        self.tableResults.setRowCount(size)
        self.fillTable(size)

    def fillTable(self, size):
        print("fill")
        self.table.setMaximumSize(size*50 + 25, size*50 + 45)
        self.tableResults.setMaximumSize(225, size * 50 + 45)
        newFont = QFont("Arial", 12)

        for i in range(size):
            for j in range(size):
                if i == j:
                    #self.table.setItem(i, j, QTableWidgetItem(QIcon("sticker.svg"), ""))
                    item = QTableWidgetItem("0")
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(newFont)
                    self.table.setItem(i, j, item)
                else:
                    item = QTableWidgetItem(str(random.randrange(1)))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(newFont)
                    self.table.setItem(i, j, item)

        self.table.setHorizontalHeaderLabels([str(i + 1) + "\n " for i in range(size)])
        print(self.table.item(0, 1).text())

        for i in range(size):
            for j in range(2):
                    item = QTableWidgetItem("__")
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(newFont)
                    self.tableResults.setItem(i, j, item)

    def solve(self):
        self.calculatProbabilities()
        self.calculateStabilisationTime()

    def calculatProbabilities(self):
        matrix = [[float(self.table.item(j, i).text()) for j in range(self.table.rowCount())]
                  for i in range(self.table.columnCount())]

        for i in range(self.table.columnCount()):
            matrix[i][i] = -sum([matrix[j][i] for j in range(self.table.columnCount())])

        #print(matrix)
        b = [0]*self.table.columnCount()
        b[0] = 1

        matrix[0] = [1 for _ in matrix[0]]
        #print(matrix)
        #print(b)

        a = numpy.array(matrix)
        b = numpy.array(b)
        answ = list(numpy.linalg.solve(a, b))
        #print(answ)

        for i in range(len(answ)):
            self.tableResults.item(i, 0).setText("{:.4f}".format(answ[i]))

    def calculateStabilisationTime(self):
        matrix = [[float(self.table.item(i, j).text()) for j in range(self.table.rowCount())]
                  for i in range(self.table.columnCount())]
        print(matrix)

        start_probabilities = [1/len(matrix[0]) for _ in matrix[0]]
        print(start_probabilities)

        limit_probabilities = calc_limit_probabilities(matrix)
        print(limit_probabilities)

        stabilization_times = calc_stabilization_times(matrix, start_probabilities, limit_probabilities)
        print(stabilization_times)

        for i in range(len(stabilization_times)):
            self.tableResults.item(i, 1).setText("{:.4f}".format(stabilization_times[i]))

TIME_DELTA = 1e-3
EPS = 1e-2


def dps(matrix, probabilities):
    n = len(matrix)
    return [
        TIME_DELTA * sum(
            [
                probabilities[j] * (-sum(matrix[i]) + matrix[i][i])
                if i == j else
                probabilities[j] * matrix[j][i]
                for j in range(n)
            ]
        )
        for i in range(n)
    ]


def calc_limit_probabilities(matrix):
    n = len(matrix)
    return numpy.linalg.solve(
        [
            [
                -sum(matrix[i]) + matrix[i][i] if i == j else matrix[j][i]
                for j in range(n)
            ]
            if i != n - 1 else [1 for j in range(n)]
            for i in range(n)
        ],
        [0 if i != n - 1 else 1 for i in range(n)]
    ).tolist()


def calc_stabilization_times(matrix, start_probabilities, limit_probabilities):
    n = len(matrix)
    current_time = 0
    current_probabilities = start_probabilities.copy()
    stabilization_times = [0 for i in range(n)]
    for c in range(10000000):
        curr_dps = dps(matrix, current_probabilities)
        for i in range(n):
            if (
                    not stabilization_times[i] and
                    abs(current_probabilities[i] - limit_probabilities[i]) <= EPS and
                    curr_dps[i] <= EPS
            ):
                stabilization_times[i] = current_time
            current_probabilities[i] += curr_dps[i]
        if all(stabilization_times):
            break
        current_time = round(current_time + TIME_DELTA, 6)
    return stabilization_times

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
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()
