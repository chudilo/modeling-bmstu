from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFont, QIcon
from PySide2.QtWidgets import (QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QFrame, QBoxLayout,
                               QAction, QTableWidget, QFormLayout, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QStyledItemDelegate)

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

        self.dataLayout = QHBoxLayout()
        self.generatorLabel = QLabel("Generator")
        self.mLabel = QLabel("\u03BC")
        self.mLine = QLineEdit("10")
        self.sigmaLabel = QLabel("\u03C3")
        self.sigmaLine = QLineEdit("2")
        self.genBox = QFormLayout()
        self.genBox.addWidget(self.generatorLabel)
        self.genBox.addRow(self.mLabel, self.mLine)
        self.genBox.addRow(self.sigmaLabel, self.sigmaLine)

        self.processorLabel = QLabel("Processor")
        self.aLabel = QLabel("a")
        self.aLine = QLineEdit("5")
        self.bLabel = QLabel("b")
        self.bLine = QLineEdit("15")
        self.procBox = QFormLayout()
        self.procBox.addWidget(self.processorLabel)
        self.procBox.addRow(self.aLabel, self.aLine)
        self.procBox.addRow(self.bLabel, self.bLine)

        self.genBox.setSpacing(10)
        self.procBox.setSpacing(10)
        self.dataLayout.addLayout(self.genBox)
        self.dataLayout.addLayout(self.procBox)
        self.dataLayout.setSpacing(30)

        self.hLayout = QHBoxLayout()

        self.numLayout = QFormLayout()
        self.numLabel = QLabel("Number of requests")
        self.numLine = QLineEdit("10000")
        self.numLayout.addWidget(self.numLabel)
        self.numLayout.addWidget(self.numLine)

        self.deltLayout = QFormLayout()
        self.deltLabel = QLabel("\u0394t")
        self.deltLine = QLineEdit("1")
        self.deltLayout.addWidget(self.deltLabel)
        self.deltLayout.addWidget(self.deltLine)

        self.numLayout.setSpacing(10)
        self.deltLayout.setSpacing(10)

        self.hLayout.addLayout(self.numLayout)
        self.hLayout.addLayout(self.deltLayout)
        self.hLayout.setSpacing(30)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addLayout(self.dataLayout)
        self.mainLayout.addWidget(line)
        self.mainLayout.addLayout(self.hLayout)
        self.mainLayout.addWidget(line1)
        self.setLayout(self.mainLayout)


        '''
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
        #self.buttonSize.clicked.connect(self.resizeTable)

        self.buttonCalculate = QPushButton("Вычислить")
        #self.buttonCalculate.clicked.connect(self.solve)
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
    '''

class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Обслуживающий аппарат")
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
