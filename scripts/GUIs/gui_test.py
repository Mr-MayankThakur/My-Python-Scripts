from PyQt5 import QtWidgets, uic

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = uic.loadUi("calci.ui")  # .ui file location here

    win.show()

    sys.exit(app.exec())