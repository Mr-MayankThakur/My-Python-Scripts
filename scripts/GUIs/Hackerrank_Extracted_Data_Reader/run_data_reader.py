from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from data_reader import Ui_MainWindow  # importing our generated file
from pygments import highlight
from pygments.lexers.python import Python3Lexer
from pygments.lexers.text import TexLexer
from pygments.formatters.html import HtmlFormatter

import sys
import json
import webbrowser


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # declaring variables which will be used while running of program
        self.json_data = None
        self.current_index = -1
        self.labels = []
        self.file_path = None

        # declaring connections of objects to functions
        self.ui.actionOpen.triggered.connect(self.triggered_action_open)

        self.ui.openFileBtn.clicked.connect(self.triggered_action_open)

        self.ui.actionReset.triggered.connect(self.triggered_action_reset)

        self.ui.actionExit.triggered.connect(self.triggered_action_exit)

        self.ui.nextBtn.clicked.connect(self.next_entry)

        self.ui.previousBtn.clicked.connect(self.previous_entry)

        self.ui.comboBox.currentIndexChanged.connect(self.open_file)

        self.ui.testCaseBtn.clicked.connect(self.download_test_case)

        self.ui.problemDownloadBtn.clicked.connect(self.download_problem_statement)

        # setting initial condition of ui components
        self.ui.nextBtn.setDisabled(True)
        self.ui.previousBtn.setDisabled(True)

    def triggered_action_exit(self):
        self.close()

    def triggered_action_open(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Hackerrank Submission Extracted Json", "", "Json Files (*.json)", options=options)

        if self.file_path is not None:
            with open(self.file_path, "r") as file:
                self.json_data = json.load(file)

        for entry in self.json_data:
            self.labels.append(entry['label'])
        self.clean_labels()
        self.ui.fileNameTextBox.setText(str(self.file_path))
        self.ui.comboBox.addItems(self.labels)
        #self.open_file()

    def clean_labels(self):
        temp_dict = dict()
        final = []
        for entry in self.labels:
            if entry in temp_dict:
                temp_dict[entry] += 1
                final.append("{} - {}".format(entry, temp_dict[entry]))
            else:
                temp_dict[entry] = 0
                final.append(entry)
        self.labels = final

    def open_file(self):
        self.current_index = self.ui.comboBox.currentIndex()
        if self.current_index == -1:
            return
        if self.current_index == 0:
            self.ui.previousBtn.setDisabled(True)
        else:
            self.ui.previousBtn.setDisabled(False)

        if self.current_index == len(self.labels)-1:
            self.ui.nextBtn.setDisabled(True)
        else:
            self.ui.nextBtn.setDisabled(False)

        self.ui.statementWebView.setHtml(highlight(self.json_data[self.current_index]['statement'], TexLexer(), HtmlFormatter(full=True, style="native")))
        self.ui.solutionWebView.setHtml(highlight(self.json_data[self.current_index]['code'], Python3Lexer(), HtmlFormatter(full=True, style="native")))
        self.ui.solutionWebView.page.toHtml(self.callable)

    def triggered_action_reset(self):
        self.json_data = None
        self.current_index = -1
        self.labels = []
        self.file_path = ""
        self.ui.comboBox.clear()
        self.ui.solutionWebView.setUrl("about:blank")
        self.ui.statementWebView.setUrl("about:blank")
        self.ui.nextBtn.setDisabled(True)
        self.ui.previousBtn.setDisabled(True)

    def callable(self, data):
        self.html = data

    def next_entry(self):
        self.ui.comboBox.setCurrentIndex(self.current_index+1)

    def previous_entry(self):
        self.ui.comboBox.setCurrentIndex(self.current_index-1)

    def download_test_case(self):
        try:
            webbrowser.open(self.json_data[self.current_index]["test_case_link"])
        except:
            pass

    def download_problem_statement(self):
        try:
            webbrowser.open(self.json_data[self.current_index]["pdf_link"])
        except:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    application = Window()

    application.show()

    sys.exit(app.exec())