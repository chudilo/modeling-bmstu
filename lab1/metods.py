import random
import math

# TODO: fillTablesTab function
class Data(object):
    def __init__(self, length):
        self.__initDataFields(length)

    def __initDataFields(self, length):
        self.length = length
        self.file = open("numbers.txt", 'r').read().split("\n")

        self.tables = dict()
        self.tables['tab'] = [[], [], []]
        self.tables['alg'] = [[], [], []]
        self.tables['hand'] = []

        self.ratings = dict()
        self.ratings['tab'] = [None, None, None]
        self.ratings['alg'] = [None, None, None]
        self.ratings['hand'] = None

    def refresh(self):
        self.fillTablesAlg(self.length)
        self.fillTablesTab(self.length)

    def fillTablesTab(self, num):
        # TODO: fillTablesTab function
        self.tables['tab'][0] = self.getTableTab(num, 0, 9)
        self.tables['tab'][1] = self.getTableTab(num, 10, 99)
        self.tables['tab'][2] = self.getTableTab(num, 100, 999)

        self.ratings['tab'][0] = self.getRating(self.tables['tab'][0])
        self.ratings['tab'][1] = self.getRating(self.tables['tab'][1])
        self.ratings['tab'][2] = self.getRating(self.tables['tab'][2])

    def getTableTab(self, num, leftBord, rightBord):
        column = random.randint(1, len(self.file[0].split())-1)
        row = random.randint(0, len(self.file)-num-1)
        arr = []
        for i in range(num):
            arr.append(int(self.file[row].split()[column]) % (rightBord - leftBord) + leftBord)
            row += 1

        return arr

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
        return Data.correlation(array)  # TODO: This is stub, place for a function that evaluates the sequence

    @staticmethod
    def correlation(array):
        n = len(array)
        arraySum = sum(array)
        res = []

        if n == 0:
            return 0

        step = int(math.log(n, math.e))

        if step < 1:
            step = 1

        for shift in range(0, n - 1, step):
            sumU1 = 0
            sumU2 = 0

            for i in range(n):
                numI = int(array[(i + shift + 1) % n])
                numJ = int(array[i])
                sumU2 += numI**2
                sumU1 += numI * numJ

            top = n * sumU1 - arraySum ** 2
            bottom = n * sumU2 - arraySum ** 2

            if bottom == 0:
                res.append(1)

            res.append(math.fabs(top / bottom))

        if res:
            return sum(res)/(len(res))
        else:
            return 1
