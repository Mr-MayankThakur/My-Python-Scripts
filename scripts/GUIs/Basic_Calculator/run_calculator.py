from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from calculator import Ui_MainWindow  # importing our generated file

import sys


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.calc_button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print(self.ui.inp1.text())
        self.showMinimized()

        # check if user has entered a number
        if self.ui.inp1.text() == "":
            self.ui.inp1.setText("0")

        if self.ui.inp2.text() == "":
            self.ui.inp2.setText("0")

        # check the operator selected and find answer
        if self.ui.comboBox.currentText() == "+":
            answer = str(int(self.ui.inp1.text()) + int(self.ui.inp2.text()))
        elif self.ui.comboBox.currentText() == "-":
            answer = str(int(self.ui.inp1.text()) - int(self.ui.inp2.text()))
        elif self.ui.comboBox.currentText() == "*":
            answer = str(int(self.ui.inp1.text()) * int(self.ui.inp2.text()))
        elif self.ui.comboBox.currentText() == "/":
            answer = str(int(self.ui.inp1.text()) / int(self.ui.inp2.text()))
        else:
            answer = "Operator Error!!"

        self.ui.label_result.setText("Answer = {}".format(answer))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    application = Window()

    application.show()

    sys.exit(app.exec())