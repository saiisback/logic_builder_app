import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def __init__(self):
        self.moving_value = 1
    def animation(self):
        self.animation = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation.setDuration(1000)
        self.animation.setEndValue(QRect(self.pushButton7.x(), self.pushButton7.y(), 90, 90))
        self.animation.start()

    def animation4(self):
        self.animation4 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation4.setDuration(1000)
        self.animation4.setEndValue(QRect(self.pushButton4.x(), self.pushButton4.y(), 90, 90))
        self.animation4.start()
        self.moving_value = self.moving_value * 2
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton4.setEnabled(False)

    def animation5(self):
        self.animation5 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation5.setDuration(1000)
        self.animation5.setEndValue(QRect(self.pushButton5.x(), self.pushButton5.y(), 90, 90))
        self.animation5.start()
        self.moving_value = self.moving_value * 3
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton5.setEnabled(False)

    def animation6(self):
        self.animation6 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation6.setDuration(1000)
        self.animation6.setEndValue(QRect(self.pushButton6.x(), self.pushButton6.y(), 90, 90))
        self.animation6.start()
        self.moving_value = self.moving_value * 5
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton6.setEnabled(False)

    def animation7(self):
        self.animation7 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation7.setDuration(1000)
        self.animation7.setEndValue(QRect(self.pushButton7.x(), self.pushButton7.y(), 90, 90))
        self.animation7.start()

    def animation8(self):
        self.animation8 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation8.setDuration(1000)
        self.animation8.setEndValue(QRect(self.pushButton8.x(), self.pushButton8.y(), 90, 90))
        self.animation8.start()

    def animation9(self):
        self.animation9 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation9.setDuration(1000)
        self.animation9.setEndValue(QRect(self.pushButton9.x(), self.pushButton9.y(), 90, 90))
        self.animation9.start()

    def animation10(self):
        self.animation10 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation10.setDuration(1000)
        self.animation10.setEndValue(QRect(self.pushButton10.x(), self.pushButton10.y(), 90, 90))
        self.animation10.start()
        self.moving_value = self.moving_value + 2
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton10.setEnabled(False)

    def animation11(self):
        self.animation11 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation11.setDuration(1000)
        self.animation11.setEndValue(QRect(self.pushButton11.x(), self.pushButton11.y(), 90, 90))
        self.animation11.start()
        self.moving_value = self.moving_value + 3
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton11.setEnabled(False)
    def animation12(self):
        self.animation12 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation12.setDuration(1000)
        self.animation12.setEndValue(QRect(self.pushButton12.x(), self.pushButton12.y(), 90, 90))
        self.animation12.start()
        self.moving_value = self.moving_value +5
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton12.setEnabled(False)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Logic builder")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setPixmap(QPixmap("task_back.jpeg"))
        self.label.setText("")
        self.label.setObjectName("label")
        self.req_output_display = QtWidgets.QLabel(self.centralwidget)
        self.req_output_display.setGeometry(1080, 360, 90, 90)
        self.req_output_display.setStyleSheet("background:pink;")
        self.req_output_display.setText("49")
        self.req_output_display.setObjectName("req_output_display")
        self.req_output_display.setStyleSheet("background-color:pink;border-radius:10%;font-size:20px")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setText("Solve the mystery of the ancient temple")
        self.label_20.setGeometry(700, 40, 361, 91)
        self.label_20.setStyleSheet("font-size:20px;")
        self.label_20.setObjectName("label_20")
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setGeometry(810, 530, 151, 31)
        self.startbutton.setObjectName("startbutton")
        self.startbutton.setText('START OVER')
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setText("EXIT")
        self.exitbutton.setGeometry(810, 580, 151, 31)
        self.exitbutton.setObjectName("exitbutton")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation4)
        self.pushButton4.setGeometry(150, 250, 90, 90)
        self.pushButton4.setText("x 2")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation5)
        self.pushButton5.setGeometry(260, 250, 90, 90)
        self.pushButton5.setText("x 3")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation6)
        self.pushButton6.setGeometry(370, 250, 90, 90)
        self.pushButton6.setText("x 5")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation7)
        self.pushButton7.setGeometry(150, 360, 90, 90)
        self.pushButton7.setText("")
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setStyleSheet("background-color:white;border-radius:10%;")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation8)
        self.pushButton8.setGeometry(260, 360, 90, 90)
        self.pushButton8.setText("")
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton8.setStyleSheet("background-color:white;border-radius:10%;")
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation9)
        self.pushButton9.setGeometry(370, 360, 90, 90)
        self.pushButton9.setText("")
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton9.setStyleSheet("background-color:white;border-radius:10%;")
        self.pushButton10 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation10)
        self.pushButton10.setGeometry(150, 470, 90, 90)
        self.pushButton10.setText("+ 2")
        self.pushButton10.setObjectName("pushButton10")
        self.pushButton10.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.pushButton11 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation11)
        self.pushButton11.setGeometry(260, 470, 90, 90)
        self.pushButton11.setText("+ 3")
        self.pushButton11.setObjectName("pushButton11")
        self.pushButton11.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.pushButton12 = QtWidgets.QPushButton(self.centralwidget, clicked=self.animation12)
        self.pushButton12.setGeometry(370, 470, 90, 90)
        self.pushButton12.setText("+ 5")
        self.pushButton12.setObjectName("pushButton12")
        self.pushButton12.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")
        self.movingbutton = QtWidgets.QPushButton(self.centralwidget)
        self.movingbutton.setGeometry(260, 360, 90, 90)
        self.movingbutton.setText("1")
        self.movingbutton.setObjectName("movingbutton")
        self.movingbutton.setStyleSheet("background-color:pink;border-radius:10%;")
        self.end_block_1 = QtWidgets.QPushButton(self.centralwidget)
        self.end_block_1.setGeometry(480, 360, 90, 90)
        self.end_block_1.setText("")
        self.end_block_1.setObjectName("end_block_1")
        self.end_block_1.setStyleSheet("background-color:white;border-radius:10%;")
        self.end_block_2 = QtWidgets.QPushButton(self.centralwidget)
        self.end_block_2.setGeometry(610, 360, 90, 90)
        self.end_block_2.setText("")
        self.end_block_2.setObjectName("end_block_2")
        self.end_block_2.setStyleSheet("background-color:white;border-radius:10%;")
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

