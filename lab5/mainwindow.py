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
        self.failLine = QLabel()
        self.failLine.setFrameShape(QFrame.WinPanel)
        self.failLine.setFrameShadow(QFrame.Raised)
        self.probLabel = QLabel("Probability of failing")
        self.probLine = QLabel()
        self.probLine.setFrameShape(QFrame.WinPanel)
        self.probLine.setFrameShadow(QFrame.Raised)
        self.answerBox = QFormLayout()
        self.answerBox.addWidget(self.answerLabel)
        self.answerBox.addRow(self.numLabel, self.numLine)
        self.answerBox.addRow(self.failLabel, self.failLine)
        self.answerBox.addRow(self.probLabel, self.probLine)

        self.button = QPushButton("Calculate")
        #self.button.clicked.connect(self.calculate)
        self.button.setMinimumSize(100,65)
        self.button.setMaximumSize(200, 65)
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


        """
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

        self.probLayout = QFormLayout()
        self.probLabel = QLabel("Probability of returning")
        self.probLine = QLineEdit("0")
        self.probLayout.addWidget(self.probLabel)
        self.probLayout.addWidget(self.probLine)


        self.numLayout.setSpacing(10)
        self.deltLayout.setSpacing(10)
        self.probLayout.setSpacing(10)

        self.hLayout.addLayout(self.numLayout)
        self.hLayout.addLayout(self.deltLayout)
        self.hLayout.addLayout(self.probLayout)
        self.hLayout.setSpacing(30)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)

        self.answerLabel = QLabel("Optimal length of queue")
        self.dtLabel = QLabel("\u0394t")
        self.dtLine = QLabel()
        self.dtLine.setFrameShape(QFrame.WinPanel)
        self.dtLine.setFrameShadow(QFrame.Raised)
        self.eventLabel = QLabel("Events")
        self.eventLine = QLabel()
        self.eventLine.setFrameShape(QFrame.WinPanel)
        self.eventLine.setFrameShadow(QFrame.Raised)
        self.answerBox = QFormLayout()
        self.answerBox.addWidget(self.answerLabel)
        self.answerBox.addRow(self.dtLabel, self.dtLine)
        self.answerBox.addRow(self.eventLabel, self.eventLine)

        self.button = QPushButton("Calculate")
        self.button.clicked.connect(self.calculate)
        self.button.setMinimumSize(100,65)
        self.button.setMaximumSize(200, 65)
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.button)
        self.buttonLayout.setAlignment(Qt.AlignBottom)

        self.answLayout = QHBoxLayout()
        self.answLayout.addLayout(self.answerBox)
        self.answLayout.addLayout(self.buttonLayout)
        #self.answLayout.setAlignment(Qt.AlignBottom)

        self.mainLayout.addLayout(self.dataLayout)
        self.mainLayout.addWidget(line)
        self.mainLayout.addLayout(self.hLayout)
        self.mainLayout.addWidget(line1)
        self.mainLayout.addLayout(self.answLayout)

        self.mainLayout.setAlignment(Qt.AlignVCenter)
        self.mainLayout.setSpacing(20)
        """



    def calculate(self):
        m = self.mLine.text()
        try:
            m = float(m)
            if m < 0:
                return
        except Exception as e:
            print(e)

        sigma = self.sigmaLine.text()
        try:
            sigma = float(sigma)
            if math.isclose(sigma, 0.0, rel_tol=1e-07, abs_tol=0.0):
                return
        except Exception as e:
            print(e)

        requestsCount = self.numLine.text()
        try:
            requestsCount = int(requestsCount)
            if requestsCount < 0:
                return

        except Exception as e:
            print(e)

        a = self.aLine.text()
        try:
            a = float(a)
            if a < 0:
                return
        except Exception as e:
            print(e)

        b = self.bLine.text()
        try:
            b = float(b)
            if b < 0:
                return
        except Exception as e:
            print(e)

        dt = self.deltLine.text()
        try:
            dt = float(dt)
            if dt < 0 or math.isclose(dt, 0.0, rel_tol=1e-07, abs_tol=0.0):
                return
        except Exception as e:
            print(e)

        pRet = self.probLine.text()
        try:
            pRet = float(pRet)
            if not -0.00000000001 < pRet <= 1.000000001:
                return
        except Exception as e:
            print(e)

        generator = Generator(m, sigma)
        processor = Processor(a, b)

        self.dtLine.setText(str(getDeltaQueue(generator, processor, requestsCount, dt, pRet)))
        self.eventLine.setText(str(getEventsQueue(generator, processor, requestsCount, pRet)))


class Generator(object):
    def __init__(self, m, sigma):
        self.__m = m
        self.__sigma = sigma

    def getWorkTime(self):
        ret = -1
        while ret < 0:
            ret = (sum([random.random() for _ in range(12)]) - 6)*self.__sigma + self.__m
            #ret = numpy.random.normal(self.__m, self.__sigma)
        return ret


class Processor(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def getWorkTime(self):
        ret = self.__a + random.random()*(self.__b - self.__a)
        return ret


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

def getDeltaQueue(generator, processor, requestsCount, dt, pRet):
    print("START DELTA")
    currTime = dt
    doneCount = 1

    queue = RequestQueue()
    generatorTime = generator.getWorkTime()
    queue.inc()

    processorTime = generatorTime + processor.getWorkTime()
    queue.dec()
    inactionF = False

    while doneCount < requestsCount:
        if currTime > generatorTime:
            generatorTime += generator.getWorkTime()
            queue.inc()

        if currTime > processorTime:
            if inactionF:
                if queue.dec():
                    processorTime = generatorTime + processor.getWorkTime()
                    #print("dec")
                    doneCount += 1
                    if random.random() < pRet:
                        queue.inc()
                        processorTime += processor.getWorkTime()
                        queue.dec()

                    inactionF = False
            else:
                if queue.dec():
                    #print("dec")
                    processorTime += processor.getWorkTime()
                    doneCount += 1
                    if random.random() < pRet:
                        queue.inc()
                        processorTime += + processor.getWorkTime()
                        queue.dec()
                else:
                    inactionF = True


        currTime += dt

    return queue.max

def getEventsQueue(generator, processor, requestsCount, pRet):
    print("START EVENT")
    doneCount = 1

    queue = RequestQueue()
    generatorTime = [generator.getWorkTime()]
    queue.inc()

    processorTime = [generatorTime[0] + processor.getWorkTime()]
    queue.dec()
    inactionF = False

    returnedRequests = []

    # Я ЗАПРОГАЛ ЭТО В 4 ЧАСА НОЧИ, ДА ЛАДНО ВАМ
    events = [generatorTime, processorTime]

    while doneCount < requestsCount:
        cur = []
        for i in range(len(events)):
            if events[i]:
                cur.append((events[i][0], i))

        mVal = cur[0][0]
        mIndex = cur[0][1]

        for i in range(len(cur)):
            if cur[i][0] < mVal:
                mVal, mIndex = cur[i][0], cur[i][1]

        event = events[mIndex][0]
        doneCount += 1

        if mIndex == 0:
            events[0].append(events[0][0] + generator.getWorkTime())
            queue.inc()
            events[0].pop(0)

        elif mIndex == 1:
            if inactionF:
                if queue.dec():
                    events[1].append(events[0][0] + processor.getWorkTime())
                    doneCount += 1
                    inactionF = False
                    events[1].pop(0)

                    if random.random() < pRet:
                        queue.inc()
                        events[1].append(events[1][0] + processor.getWorkTime())
                        events[1].pop(0)
                        #Здесь был костыль
            else:
                if queue.dec():
                    events[1].append(events[1][0] + processor.getWorkTime())
                    doneCount += 1
                    events[1].pop(0)

                    if random.random() < pRet:
                        queue.inc()
                        events[1].append(events[1][0] + processor.getWorkTime())
                        events[1].pop(0)
                else:
                    inactionF = True
                    events[1].append(events[0][-1])
                    events[1].pop(0)


    return queue.max

'''
    
    def event_based_modelling(self, a, b, lmbda):
        req_generator = PoissonGenerator(lmbda)
        req_proccessor = UniformGenerator(a, b)
    
        req_done_count = 0
        t_generation = req_generator.generate()
        t_proccessor = t_generation + req_proccessor.generate()
    
        while t_proccessor < self.req_count:
            if t_generation <= t_proccessor:
                self.add_to_queue()
                t_generation += req_generator.generate()
            if t_generation >= t_proccessor:
                req_done_count += self.rem_from_queue()
                t_proccessor += req_proccessor.generate()
    
        return self.queue_len_max, req_done_count, self.reenter
    
    def time_based_modelling(self, a, b, lmbda):
    
        req_generator = PoissonGenerator(lmbda)
        req_proccessor = UniformGenerator(a, b)
    
        req_done_count = 0
        t_generation = req_generator.generate()
        t_proccessor = t_generation + req_proccessor.generate()
    
        t_curr = 0
        while t_curr < self.req_count:
            # while t_curr < 5500:
            if t_generation <= t_curr:
                self.add_to_queue()
                t_generation += req_generator.generate()
            if t_proccessor <= t_curr:
                req_done_count += self.rem_from_queue()
                t_proccessor += req_proccessor.generate()
    
            t_curr += self.dt
        return self.queue_len_max, req_done_count, self.reenter

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
