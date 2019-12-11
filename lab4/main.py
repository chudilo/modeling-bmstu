from mainwindow import MainWindow, ServingMachineStatistics
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QFont
import sys


def main():
    app = QApplication(sys.argv)

    widget = ServingMachineStatistics()
    newFont = QFont("Arial", 14)
    widget.setFont(newFont)

    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
