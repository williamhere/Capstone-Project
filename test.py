from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 842)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(30, 750, 151, 41))
        self.start.setObjectName("start")
        self.start.setFont(QFont('Arial', 16))

        self.tv = QtWidgets.QLabel(self.centralwidget)
        self.tv.setGeometry(QtCore.QRect(30, 20, 781, 691))
        self.tv.setFrameShape(QtWidgets.QFrame.Box)
        self.tv.setText("")
        self.tv.setObjectName("tv")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 750, 421, 41))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setFont(QFont('Arial', 16))
        self.label.setObjectName("label")

        self.finish = QtWidgets.QPushButton(self.centralwidget)
        self.finish.setGeometry(QtCore.QRect(200, 750, 141, 41))
        self.finish.setObjectName("finish")
        self.finish.setFont(QFont('Arial', 16))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.finish.setText(_translate("MainWindow", "Finish"))