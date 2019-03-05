
from PyQt5 import QtCore, QtGui, QtWidgets


class CalculatorUi(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(474, 176)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(474, 176))
        MainWindow.setMaximumSize(QtCore.QSize(474, 176))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 171))
        self.formLayoutWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_equals = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_equals.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_equals.setText("")
        self.label_equals.setAlignment(QtCore.Qt.AlignCenter)
        self.label_equals.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_equals.setObjectName("label_equals")
        self.gridLayout.addWidget(self.label_equals, 3, 1, 1, 1)
        self.title = QtWidgets.QLabel(self.formLayoutWidget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_credit = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_credit.setObjectName("label_credit")
        self.gridLayout.addWidget(self.label_credit, 4, 2, 1, 1)
        self.label_result = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 3, 0, 1, 1)
        self.calc_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.calc_button.setObjectName("calc_button")
        self.gridLayout.addWidget(self.calc_button, 2, 0, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.inp2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp2.setMinimumSize(QtCore.QSize(100, 30))
        self.inp2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inp2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inp2.setText("")
        self.inp2.setMaxLength(999999999)
        self.inp2.setAlignment(QtCore.Qt.AlignCenter)
        self.inp2.setClearButtonEnabled(False)
        self.inp2.setObjectName("inp2")
        self.gridLayout.addWidget(self.inp2, 1, 2, 1, 1)
        self.label_answer = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_answer.sizePolicy().hasHeightForWidth())
        self.label_answer.setSizePolicy(sizePolicy)
        self.label_answer.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_answer.setText("")
        self.label_answer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_answer.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_answer.setObjectName("label_answer")
        self.gridLayout.addWidget(self.label_answer, 3, 2, 1, 1)
        self.inp1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inp1.setMinimumSize(QtCore.QSize(100, 30))
        self.inp1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inp1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inp1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.inp1.setText("")
        self.inp1.setMaxLength(999999999)
        self.inp1.setAlignment(QtCore.Qt.AlignCenter)
        self.inp1.setObjectName("inp1")
        self.gridLayout.addWidget(self.inp1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic Calculator"))
        self.title.setText(_translate("MainWindow", "Basic Calculator"))
        self.label_credit.setText(_translate("MainWindow", "Made By - Mayank Thakur"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.inp2.setPlaceholderText(_translate("MainWindow", "Number 2"))
        self.inp1.setStatusTip(_translate("MainWindow", "Number1"))
        self.inp1.setWhatsThis(_translate("MainWindow", "Number 1"))
        self.inp1.setPlaceholderText(_translate("MainWindow", "Number 1"))

