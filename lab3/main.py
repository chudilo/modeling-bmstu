from mainwindow import MainWindow, Table
from PySide2.QtWidgets import QApplication, QLabel
import pyqtgraph as pg

import sys


def main():
    app = QApplication(sys.argv)

    window = MainWindow(Table())
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
