# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'release_first.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#这是UI的初稿
#变量介绍：
#不需要编程的变量：
#两个纯展示不需要动的变量：textWeather，textdate

#需要编程的变量：
#两个按钮，分别对应展示天气和展示搭配：btnTianqi  btnDapei
#三个label，展示今天的天气状况：showRiqi showTianqi showWendu
#一个label，展示今日的搭配：showDapei
#一个label，展示今日的时间：showDate

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QTimer,Qt,QCoreApplication

import sys
import os

import get_weather, get_recommend, speech_recognition

import platform
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel,QMainWindow)



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.resize(480, 320)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 207, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Textdate = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.Textdate.setFont(font)
        self.Textdate.setTextFormat(QtCore.Qt.AutoText)
        self.Textdate.setObjectName("Textdate")
        self.verticalLayout.addWidget(self.Textdate)
        self.showDate = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.showDate.setFont(font)
        self.showDate.setObjectName("showDate")
        self.verticalLayout.addWidget(self.showDate)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showRiqi = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.showRiqi.setFont(font)
        self.showRiqi.setObjectName("showRiqi")
        self.horizontalLayout.addWidget(self.showRiqi)
        self.showTianqi = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.showTianqi.setFont(font)
        self.showTianqi.setObjectName("showTianqi")
        self.horizontalLayout.addWidget(self.showTianqi)
        self.showWendu = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.showWendu.setFont(font)
        self.showWendu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.showWendu.setObjectName("showWendu")
        self.horizontalLayout.addWidget(self.showWendu)
        self.textWeather = QtWidgets.QLabel(Form)
        self.textWeather.setGeometry(QtCore.QRect(10, 110, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.textWeather.setFont(font)
        self.textWeather.setObjectName("textWeather")
        self.showDapei = QtWidgets.QLabel(Form)
        self.showDapei.setGeometry(QtCore.QRect(10, 220, 321, 50))
        self.showDapei.setWordWrap(True)
        self.showDapei.setAlignment(Qt.AlignTop)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.showDapei.setFont(font)
        self.showDapei.setObjectName("showDapei")
        self.btnTianqi = QtWidgets.QPushButton(Form)
        self.btnTianqi.setGeometry(QtCore.QRect(40, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.btnTianqi.setFont(font)
        self.btnTianqi.setObjectName("btnTianqi")
        self.btnTianqi.clicked.connect(self.fShowtianqi)
        self.btnDapei = QtWidgets.QPushButton(Form)
        self.btnDapei.setGeometry(QtCore.QRect(250, 260, 121, 41))
        self.btnDapei.clicked.connect(self.fShowdapei)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.btnDapei.setFont(font)
        self.btnDapei.setObjectName("btnDapei")

        #新增1：退出程序
        self.Qbtn = QtWidgets.QPushButton(Form)
        self.Qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.Qbtn.setGeometry(QtCore.QRect(40, 40, 40, 40))
        self.Qbtn.setIcon(QtGui.QIcon('image\quit.png'))
        self.Qbtn.move(430, 100)

        #新增2：关闭电源
        self.Poff = QtWidgets.QPushButton(Form)
        self.Poff.clicked.connect(self.powerOff)
        self.Poff.setGeometry(QtCore.QRect(40, 40, 40, 40))
        self.Poff.setIcon(QtGui.QIcon('image\poweroff.png'))
        self.Poff.move(430, 0)

        #新增3：录音并上传识别
        self.reco = QtWidgets.QPushButton(Form)
        self.reco.clicked.connect(self.record)
        self.reco.setGeometry(QtCore.QRect(40, 40, 40, 40))
        self.reco.setIcon(QtGui.QIcon('image/record.png'))
        self.reco.move(430, 200)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #以上是初始化函数，自动生成的代码
        #以下是自己写的connect，后面找个时间重构

        #新建一个计时器，1秒运行一次fShowDate函数更新当前时间
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.fShowDate)
        self.timer1.start(1000)

        #用于获取天气按钮的CD时间，防止封IP
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.btnEnable)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Textdate.setText(_translate("Form", "DATE＆TIME"))
        self.showDate.setText(_translate("Form", "1970年12月20号 12：00"))
        self.showRiqi.setText(_translate("Form", "日期"))
        self.showTianqi.setText(_translate("Form", "天气"))
        self.showWendu.setText(_translate("Form", "温度"))
        self.textWeather.setText(_translate("Form", "WEATHER"))
        self.showDapei.setText(_translate("Form", "今日搭配"))
        self.btnTianqi.setText(_translate("Form", "获取天气"))
        self.btnDapei.setText(_translate("Form", "获取搭配"))

    #以上是pyuic自动生成的代码
    #在ui_form这个大类里继续实现各种功能


    #功能1：时间:

    def fShowDate(self):
        datatime = QDateTime.currentDateTime() #获取当前日期时间
        timeText = datatime.toString()
        self.showDate.setText(timeText)

    #功能2：获取天气
    # btnTianqi showRiqi showTianqi showWendu

    def fShowtianqi(self):
            #和风天气API传过来的列表依次是：状态码0 城市1 日期2 最高温3 最低温4 白天天气5 晚上天气6
            L1 = get_weather.GetTianqi()
            if L1[0] == 200:
                self.showRiqi.setText(L1[2])
                #如果白天和晚上的天气是一样的，就不要‘转’字了
                if L1[5]!=L1[6]:
                    self.showTianqi.setText(L1[5]+'转'+L1[6])
                else:
                    self.showTianqi.setText(L1[5])
                self.showWendu.setText(L1[3]+'℃/'+L1[4]+'℃')
                self.btnTianqi.setEnabled(False)
                #这里后面可以加入按钮颜色的改变
                self.timer2.start(5000)
            else:
                self.showRiqi.setText("404 check your network") # 获取天气数据失败，请检查原因
                self.showTianqi.setText(" ")
                self.showWendu.setText(" ")

    def btnEnable(self):
        self.btnTianqi.setEnabled(True)
        #间隔5秒后按钮恢复有效，所以是一次性的,要把timer给停了
        self.timer2.stop()

    def fShowdapei(self):
        dapei = get_recommend.getDapei()
        self.showDapei.setText(dapei)

    def powerOff(self):
        if platform.system() != 'Windows':  # 如果是windows系统就不能用这条指令了
            os.system("sudo poweroff")  # linux关机
        else:
            self.showDapei.setText('This is windows!')

    def record(self):
        #按下按键后：录音，保存在本地的指定wav
        speech_recognition.record()
        #录完音：把指令wav上传识别
        speech_recognition.shibie()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 所有界面元素的基类Qwigest ，作为对比，Qmainwindow 是一个窗口
    main = QMainWindow()
    ui = Ui_Form()
    content = ui.setupUi(main)
    main.show()

    # 确保干净退出，必有语句
    sys.exit(app.exec_())

