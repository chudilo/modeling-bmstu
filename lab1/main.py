import sys
from PySide2.QtWidgets import QApplication

from mainwindow import RandomNumbersWidget, MainWindow


def main():
    app = QApplication(sys.argv)

    widget = RandomNumbersWidget()

    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
