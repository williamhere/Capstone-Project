import sys 
import os
import test as ui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import threading

def _detect():
    os.system("python3 pose_camera.py")

t = threading.Thread(target=_detect)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.uiMain=ui.Ui_MainWindow()
        self.uiMain.setupUi(self)
        self.setWindowTitle('Pose Detection')
        self.counter = 0
        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.onTimer)
        self.mytimer.start(400)
        self.uiMain.start.clicked.connect(self.onButtonClick)
        self.uiMain.finish.clicked.connect(self.onButtonClick1)
           
    def onButtonClick(self):
        t.start()
        
    def onButtonClick1(self):
        os._exit(0)
    
    def onTimer(self):
        #path1='/home/pi/Desktop/project-posenet-master/normal.txt/'
        #path2='/home/pi/Desktop/project-posenet-master/hunchback.txt/'
        path1 = "normal.txt"
        path2 = "hunchback.txt"
        self.counter += 1
        print("Timer "+str(self.counter))
           
        isExist =os.path.exists(path2)
        isExist1 =os.path.exists(path1)
        if isExist==True:
            self.uiMain.label.setText("Pose:Hunchback")
        elif isExist1==True:
            self.uiMain.label.setText("Pose:Normal")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())