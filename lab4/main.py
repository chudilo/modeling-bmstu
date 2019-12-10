from mainwindow import MainWindow, ServingMachineStatistics
from PySide2.QtWidgets import QApplication, QLabel

import sys


def main():
    app = QApplication(sys.argv)

    window = MainWindow(ServingMachineStatistics())
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
