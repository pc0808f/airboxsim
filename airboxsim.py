# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'airboxsim.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 919)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setValueBn = QtWidgets.QPushButton(self.centralwidget)
        self.setValueBn.setGeometry(QtCore.QRect(1030, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.setValueBn.setFont(font)
        self.setValueBn.setObjectName("setValueBn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1001, 577))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TVOC_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.TVOC_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TVOC_value_2.setObjectName("TVOC_value_2")
        self.gridLayout_2.addWidget(self.TVOC_value_2, 11, 4, 1, 1)
        self.CO_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CO_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CO_value_2.setObjectName("CO_value_2")
        self.gridLayout_2.addWidget(self.CO_value_2, 9, 4, 1, 1)
        self.NO2_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.NO2_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.NO2_value_2.setObjectName("NO2_value_2")
        self.gridLayout_2.addWidget(self.NO2_value_2, 13, 4, 1, 1)
        self.MQTTser_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.MQTTser_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MQTTser_value_2.setObjectName("MQTTser_value_2")
        self.gridLayout_2.addWidget(self.MQTTser_value_2, 0, 4, 1, 1)
        self.PM2p5_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.PM2p5_input_2.setFont(font)
        self.PM2p5_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PM2p5_input_2.setObjectName("PM2p5_input_2")
        self.gridLayout_2.addWidget(self.PM2p5_input_2, 6, 1, 1, 1)
        self.O3_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.O3_input_2.setFont(font)
        self.O3_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.O3_input_2.setObjectName("O3_input_2")
        self.gridLayout_2.addWidget(self.O3_input_2, 8, 1, 1, 1)
        self.O3_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.O3_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.O3_input_3.setObjectName("O3_input_3")
        self.gridLayout_2.addWidget(self.O3_input_3, 8, 2, 1, 1)
        self.Temp_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Temp_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_value_2.setObjectName("Temp_value_2")
        self.gridLayout_2.addWidget(self.Temp_value_2, 4, 4, 1, 1)
        self.CO2_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CO2_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CO2_value_2.setObjectName("CO2_value_2")
        self.gridLayout_2.addWidget(self.CO2_value_2, 10, 4, 1, 1)
        self.PM10_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PM10_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PM10_value_2.setObjectName("PM10_value_2")
        self.gridLayout_2.addWidget(self.PM10_value_2, 7, 4, 1, 1)
        self.BoxMAC_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.BoxMAC_input_2.setFont(font)
        self.BoxMAC_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BoxMAC_input_2.setObjectName("BoxMAC_input_2")
        self.gridLayout_2.addWidget(self.BoxMAC_input_2, 1, 1, 1, 1)
        self.NO2_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NO2_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.NO2_input_3.setObjectName("NO2_input_3")
        self.gridLayout_2.addWidget(self.NO2_input_3, 13, 2, 1, 1)
        self.CH2O_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.CH2O_input_2.setFont(font)
        self.CH2O_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CH2O_input_2.setObjectName("CH2O_input_2")
        self.gridLayout_2.addWidget(self.CH2O_input_2, 12, 1, 1, 1)
        self.Temp_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Temp_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_input_3.setObjectName("Temp_input_3")
        self.gridLayout_2.addWidget(self.Temp_input_3, 4, 2, 1, 1)
        self.CO_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.CO_input_2.setFont(font)
        self.CO_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CO_input_2.setObjectName("CO_input_2")
        self.gridLayout_2.addWidget(self.CO_input_2, 9, 1, 1, 1)
        self.PM2p5_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PM2p5_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.PM2p5_input_3.setObjectName("PM2p5_input_3")
        self.gridLayout_2.addWidget(self.PM2p5_input_3, 6, 2, 1, 1)
        self.PM10_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.PM10_input_2.setFont(font)
        self.PM10_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PM10_input_2.setObjectName("PM10_input_2")
        self.gridLayout_2.addWidget(self.PM10_input_2, 7, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 7, 0, 1, 1)
        self.RH_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.RH_input_2.setFont(font)
        self.RH_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.RH_input_2.setObjectName("RH_input_2")
        self.gridLayout_2.addWidget(self.RH_input_2, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.CO2_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CO2_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CO2_input_3.setObjectName("CO2_input_3")
        self.gridLayout_2.addWidget(self.CO2_input_3, 10, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 12, 0, 1, 1)
        self.srReadMode_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.srReadMode_input_2.setFont(font)
        self.srReadMode_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.srReadMode_input_2.setObjectName("srReadMode_input_2")
        self.gridLayout_2.addWidget(self.srReadMode_input_2, 2, 1, 1, 1)
        self.TVOC_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TVOC_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.TVOC_input_3.setObjectName("TVOC_input_3")
        self.gridLayout_2.addWidget(self.TVOC_input_3, 11, 2, 1, 1)
        self.PM2p5_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PM2p5_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PM2p5_value_2.setObjectName("PM2p5_value_2")
        self.gridLayout_2.addWidget(self.PM2p5_value_2, 6, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.RH_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.RH_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.RH_input_3.setObjectName("RH_input_3")
        self.gridLayout_2.addWidget(self.RH_input_3, 5, 2, 1, 1)
        self.NO2_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.NO2_input_2.setFont(font)
        self.NO2_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.NO2_input_2.setObjectName("NO2_input_2")
        self.gridLayout_2.addWidget(self.NO2_input_2, 13, 1, 1, 1)
        self.idNum_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.idNum_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.idNum_value_2.setObjectName("idNum_value_2")
        self.gridLayout_2.addWidget(self.idNum_value_2, 3, 4, 1, 1)
        self.CH2O_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CH2O_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CH2O_value_2.setObjectName("CH2O_value_2")
        self.gridLayout_2.addWidget(self.CH2O_value_2, 12, 4, 1, 1)
        self.Temp_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Temp_input_2.setFont(font)
        self.Temp_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_input_2.setObjectName("Temp_input_2")
        self.gridLayout_2.addWidget(self.Temp_input_2, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)
        self.CH2O_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CH2O_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CH2O_input_3.setObjectName("CH2O_input_3")
        self.gridLayout_2.addWidget(self.CH2O_input_3, 12, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 8, 0, 1, 1)
        self.srReadMode_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.srReadMode_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.srReadMode_value_2.setObjectName("srReadMode_value_2")
        self.gridLayout_2.addWidget(self.srReadMode_value_2, 2, 4, 1, 1)
        self.O3_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.O3_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.O3_value_2.setObjectName("O3_value_2")
        self.gridLayout_2.addWidget(self.O3_value_2, 8, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 9, 0, 1, 1)
        self.PM10_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PM10_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.PM10_input_3.setObjectName("PM10_input_3")
        self.gridLayout_2.addWidget(self.PM10_input_3, 7, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 11, 0, 1, 1)
        self.RH_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.RH_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.RH_value_2.setObjectName("RH_value_2")
        self.gridLayout_2.addWidget(self.RH_value_2, 5, 4, 1, 1)
        self.idNum_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.idNum_input_2.setFont(font)
        self.idNum_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.idNum_input_2.setObjectName("idNum_input_2")
        self.gridLayout_2.addWidget(self.idNum_input_2, 3, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 10, 0, 1, 1)
        self.BoxMAC_value_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BoxMAC_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BoxMAC_value_2.setObjectName("BoxMAC_value_2")
        self.gridLayout_2.addWidget(self.BoxMAC_value_2, 1, 4, 1, 1)
        self.TVOC_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.TVOC_input_2.setFont(font)
        self.TVOC_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TVOC_input_2.setObjectName("TVOC_input_2")
        self.gridLayout_2.addWidget(self.TVOC_input_2, 11, 1, 1, 1)
        self.CO_input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CO_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CO_input_3.setObjectName("CO_input_3")
        self.gridLayout_2.addWidget(self.CO_input_3, 9, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 13, 0, 1, 1)
        self.CO2_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.CO2_input_2.setFont(font)
        self.CO2_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CO2_input_2.setObjectName("CO2_input_2")
        self.gridLayout_2.addWidget(self.CO2_input_2, 10, 1, 1, 1)
        self.MQTTser_input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.MQTTser_input_2.setFont(font)
        self.MQTTser_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MQTTser_input_2.setObjectName("MQTTser_input_2")
        self.gridLayout_2.addWidget(self.MQTTser_input_2, 0, 1, 1, 1)
        self.Temp_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Temp_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp_input_4.setObjectName("Temp_input_4")
        self.gridLayout_2.addWidget(self.Temp_input_4, 4, 3, 1, 1)
        self.RH_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.RH_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.RH_input_4.setObjectName("RH_input_4")
        self.gridLayout_2.addWidget(self.RH_input_4, 5, 3, 1, 1)
        self.PM2p5_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PM2p5_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.PM2p5_input_4.setObjectName("PM2p5_input_4")
        self.gridLayout_2.addWidget(self.PM2p5_input_4, 6, 3, 1, 1)
        self.PM10_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PM10_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.PM10_input_4.setObjectName("PM10_input_4")
        self.gridLayout_2.addWidget(self.PM10_input_4, 7, 3, 1, 1)
        self.O3_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.O3_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.O3_input_4.setObjectName("O3_input_4")
        self.gridLayout_2.addWidget(self.O3_input_4, 8, 3, 1, 1)
        self.CO_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CO_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.CO_input_4.setObjectName("CO_input_4")
        self.gridLayout_2.addWidget(self.CO_input_4, 9, 3, 1, 1)
        self.CO2_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CO2_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.CO2_input_4.setObjectName("CO2_input_4")
        self.gridLayout_2.addWidget(self.CO2_input_4, 10, 3, 1, 1)
        self.TVOC_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TVOC_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.TVOC_input_4.setObjectName("TVOC_input_4")
        self.gridLayout_2.addWidget(self.TVOC_input_4, 11, 3, 1, 1)
        self.CH2O_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CH2O_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.CH2O_input_4.setObjectName("CH2O_input_4")
        self.gridLayout_2.addWidget(self.CH2O_input_4, 12, 3, 1, 1)
        self.NO2_input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.NO2_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.NO2_input_4.setObjectName("NO2_input_4")
        self.gridLayout_2.addWidget(self.NO2_input_4, 13, 3, 1, 1)
        self.connectBn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBn.setGeometry(QtCore.QRect(1030, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.connectBn.setFont(font)
        self.connectBn.setObjectName("connectBn")
        self.consoleOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.consoleOutput.setGeometry(QtCore.QRect(20, 610, 1121, 261))
        self.consoleOutput.setObjectName("consoleOutput")
        self.disconnectBn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectBn.setGeometry(QtCore.QRect(1030, 560, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.disconnectBn.setFont(font)
        self.disconnectBn.setObjectName("disconnectBn")
        self.AutoBn = QtWidgets.QPushButton(self.centralwidget)
        self.AutoBn.setGeometry(QtCore.QRect(1030, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.AutoBn.setFont(font)
        self.AutoBn.setObjectName("AutoBn")
        self.timerinv = QtWidgets.QLineEdit(self.centralwidget)
        self.timerinv.setGeometry(QtCore.QRect(1030, 220, 113, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(36)
        self.timerinv.setFont(font)
        self.timerinv.setAlignment(QtCore.Qt.AlignCenter)
        self.timerinv.setObjectName("timerinv")
        self.AutoCloseBn = QtWidgets.QPushButton(self.centralwidget)
        self.AutoCloseBn.setGeometry(QtCore.QRect(1030, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.AutoCloseBn.setFont(font)
        self.AutoCloseBn.setObjectName("AutoCloseBn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 21))
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
        self.setValueBn.setText(_translate("MainWindow", "送出"))
        self.TVOC_value_2.setText(_translate("MainWindow", "0"))
        self.CO_value_2.setText(_translate("MainWindow", "0"))
        self.NO2_value_2.setText(_translate("MainWindow", "0"))
        self.MQTTser_value_2.setText(_translate("MainWindow", "255.255.255.255"))
        self.Temp_value_2.setText(_translate("MainWindow", "0"))
        self.CO2_value_2.setText(_translate("MainWindow", "0"))
        self.PM10_value_2.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "PM10"))
        self.label_18.setText(_translate("MainWindow", "idNum"))
        self.label_16.setText(_translate("MainWindow", "MQTT主機"))
        self.label_25.setText(_translate("MainWindow", "PM2.5"))
        self.label_19.setText(_translate("MainWindow", "CH2O"))
        self.PM2p5_value_2.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "空氣盒子MAC"))
        self.NO2_input_2.setText(_translate("MainWindow", "65535"))
        self.idNum_value_2.setText(_translate("MainWindow", "0"))
        self.CH2O_value_2.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "srReadMode"))
        self.label_22.setText(_translate("MainWindow", "O3"))
        self.srReadMode_value_2.setText(_translate("MainWindow", "0"))
        self.O3_value_2.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "CO"))
        self.label_20.setText(_translate("MainWindow", "TVOC"))
        self.RH_value_2.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "RH"))
        self.label_17.setText(_translate("MainWindow", "Temp"))
        self.label_27.setText(_translate("MainWindow", "CO2"))
        self.BoxMAC_value_2.setText(_translate("MainWindow", "00:11:22:33:44:55:66"))
        self.label_21.setText(_translate("MainWindow", "NO2"))
        self.Temp_input_4.setText(_translate("MainWindow", "0.1"))
        self.connectBn.setText(_translate("MainWindow", "Connect"))
        self.disconnectBn.setText(_translate("MainWindow", "Disonnect"))
        self.AutoBn.setText(_translate("MainWindow", "打開自動"))
        self.timerinv.setText(_translate("MainWindow", "3"))
        self.AutoCloseBn.setText(_translate("MainWindow", "關閉自動"))
