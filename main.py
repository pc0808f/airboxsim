import queue
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import paho.mqtt.client as mqtt
import logging

import airboxsim as ui

import configparser

# default logging output
log = logging.getLogger('main')

# logger to pass to the MQTT library
mqtt_log = logging.getLogger('mqtt')
mqtt_log.setLevel(logging.WARNING)

mqtt_rc_codes = ['Success', 'Incorrect protocol version', 'Invalid client identifier', 'Server unavailable',
                 'Bad username or password', 'Not authorized']

config = configparser.RawConfigParser()
config.read('example.cfg')

if config.has_section('Section1'):
    print("has")
    if config.has_option('Section1', 'MAC'):
        print(config.get('Section1', 'MAC', raw=True))
    else:
        config.set('Section1', 'MAC', '00:11:22:33:44:55')
else:
    config.add_section('Section1')
    config.set('Section1', 'MAC', '00:11:22:33:44:55')
    config.set('Section1', 'srreadmode', '1')
    config.set('Section1', 'idnum', '0')
    config.set('Section1', 'temp', '25.5')
    config.set('Section1', 'RH', '70')
    config.set('Section1', 'PM2.5', '0')
    config.set('Section1', 'PM10', '0')
    config.set('Section1', 'O3', '0')
    config.set('Section1', 'CO', '0')
    config.set('Section1', 'CO2', '0')
    config.set('Section1', 'TVOC', '0')
    config.set('Section1', 'HCHO', '0')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectBn.clicked.connect(self.connectBnonClick)
        self.disconnectBn.clicked.connect(self.disconnectBnonClick)
        self.setValueBn.clicked.connect(self.setValueBnOnClick)
        self.console_queue = queue.Queue()
        self._handler = None
        self.enable_console_logging()
        self.show()
        self.console_timer = QtCore.QTimer()
        self.console_timer.timeout.connect(self._poll_console_queue)
        self.console_timer.start(50)  # units are milliseconds



        self.MQTTser_input_2.setText("103.29.70.99")
        self.BoxMAC_input_2.setText(config.get('Section1', 'MAC', raw=False))
        self.BoxMAC_value_2.setText(config.get('Section1', 'MAC', raw=False))
        self.srReadMode_input_2.setText(config.get('Section1', 'srreadmode', raw=False))
        self.idNum_input_2.setText(config.get('Section1', 'idnum', raw=False))
        self.Temp_input_2.setText(config.get('Section1', 'Temp', raw=False))
        self.Temp_input_3.setText("25")
        self.Temp_input_4.setText("0")
        self.RH_input_2.setText(config.get('Section1', 'rh', raw=False))
        self.RH_input_3.setText("70")
        self.RH_input_4.setText("0")
        self.PM2p5_input_2.setText(config.get('Section1', 'pm2.5', raw=False))
        self.PM2p5_input_3.setText("1000")
        self.PM2p5_input_4.setText("0")
        self.PM10_input_2.setText(config.get('Section1', 'pm10', raw=False))
        self.PM10_input_3.setText("1000")
        self.PM10_input_4.setText("0")
        self.O3_input_2.setText(config.get('Section1', 'o3', raw=False))
        self.O3_input_3.setText("0.02")
        self.O3_input_4.setText("0")
        self.CO_input_2.setText(config.get('Section1', 'co', raw=False))
        self.CO_input_3.setText("0")
        self.CO_input_4.setText("0")
        self.CO2_input_2.setText(config.get('Section1', 'co2', raw=False))
        self.CO2_input_3.setText("300")
        self.CO2_input_4.setText("0")
        self.TVOC_input_2.setText(config.get('Section1', 'tvoc', raw=False))
        self.TVOC_input_3.setText("1000")
        self.TVOC_input_4.setText("0")
        self.CH2O_input_2.setText(config.get('Section1', 'hcho', raw=False))
        self.CH2O_input_3.setText("0.101")
        self.CH2O_input_4.setText("0")

        return

    # 當地端程式連線伺服器得到回應時，要做的動作
    ################################################################
    # The callback for when the broker responds to our connection request.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server with with flags: %s, result code: %s" % (flags, rc))
        print(rc)

        if rc == 0:
            log.info("Connection succeeded.")

        elif rc > 0:
            if rc < len(mqtt_rc_codes):
                log.warning("Connection failed with error: %s", mqtt_rc_codes[rc])
            else:
                log.warning("Connection failed with unknown error %d", rc)

        # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
        client.subscribe("#")
        self.show_status("Connected.")

        # self.set_connected_state(True)
        return

    def show_status(self, string):
        self.statusbar.showMessage(string)

    # 當接收到從伺服器發送的訊息時要進行的動作
    def on_message(self, client, userdata, msg):

        # 轉換編碼utf-8才看得懂中文
        # print(msg.topic + " " + msg.payload.decode('utf-8'))
        self.write("{%s} %s" % (msg.topic, msg.payload))
        return

    # --- logging to screen -------------------------------------------------------------
    def enable_console_logging(self):
        # get the root logger to receive all logging traffic
        logger = logging.getLogger()
        # create a logging handler which writes to the console window via self.write
        handler = logging.StreamHandler(self)
        handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        # logger.setLevel(logging.NOTSET)
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.NOTSET)
        self._handler = handler
        log.info("Enabled logging in console window.")
        log.info("test")
        return

    def write(self, string):
        """Write output to the console text area in a thread-safe way.  Qt only allows
        calls from the main thread, but the service routines run on separate threads."""
        self.console_queue.put(string)
        return

    def disable_console_logging(self):
        if self._handler is not None:
            logging.getLogger().removeHandler(self._handler)
            self._handler = None

    def connectBnonClick(self):
        print("Hello")

        # 連線設定
        # 初始化地端程式
        self.client = mqtt.Client()

        # 設定連線的動作
        self.client.on_connect = self.on_connect

        # 設定接收訊息的動作
        self.client.on_message = self.on_message

        # 設定登入帳號密碼
        # client.username_pw_set("try", "xxxx")

        # 設定連線資訊(IP, Port, 連線時間)
        self.client.connect("103.29.70.99", 1883, 60)

        # 開始連線，執行設定的動作和處理重新連線問題
        # 也可以手動使用其他loop函式來進行連接
        self.client.loop_start()
        return

    def disconnectBnonClick(self):

        self.client.disconnect()
        return

    def setValueBnOnClick(self):

        pCMD=0
        psrReadMode= self.srReadMode_input_2.text()
        pIdNum=self.idNum_input_2.text()
        pTemp=self.Temp_input_2.text()
        pRH=self.RH_input_2.text()
        pPM2p5=self.PM2p5_input_2.text()
        pPM10=self.PM10_input_2.text()
        pO3=self.O3_input_2.text()
        pCO=self.CO_input_2.text()
        pCO2=self.CO2_input_2.text()
        pTVOC=self.TVOC_input_2.text()
        pCH2O=self.CH2O_input_2.text()
        pNO2=self.NO2_input_2.text()


        if self.client.is_connected():
            pubTopic = self.BoxMAC_value_2.text() + "_DEV"
            pubPayload = '"CMD": {CMD}, "srReadMode":{srReadMode}, "IdNum":{IdNum}, "Temp":{Temp}, "RH":{RH}, ' \
                '"PM2p5":{PM2p5},"PM10":{PM10},"O3":{O3},"CO":{CO},"CO2":{CO2},"TVOC":{TVOC},"CH2O":{' \
                'CH2O},"NO2":{NO2}'.format(CMD=pCMD, srReadMode=psrReadMode, IdNum=pIdNum, Temp=pTemp, RH=pRH,
                                           PM2p5=pPM2p5, PM10=pPM10, O3=pO3, CO=pCO, CO2=pCO2, TVOC=pTVOC, CH2O=pCH2O,
                                           NO2=pNO2)
            # pubPayload='"CMD": {CMD}'.format(CMD=0)
            self.Temp_value_2.setText(pTemp)
            self.RH_value_2.setText(pRH)
            self.PM2p5_value_2.setText(pPM2p5)
            self.PM10_value_2.setText(pPM10)
            self.O3_value_2.setText(pO3)
            self.CO_value_2.setText(pCO)
            self.CO2_value_2.setText(pCO2)
            self.TVOC_value_2.setText(pTVOC)
            self.CH2O_value_2.setText(pCH2O)
            self.NO2_value_2.setText(pNO2)

            pubPayload= '{' + pubPayload + '}'
            print(pubPayload)
            self.client.publish(pubTopic, pubPayload)
        else:
            self.window.write("Not connected.")

        pIdNum = str(int(pIdNum) + 1)
        self.idNum_input_2.setText(pIdNum)
        config.set('Section1', 'idnum', pIdNum)

        #Temp

        addValue = float(self.Temp_input_4.text())
        if addValue > 0:
            pTemp = round(float(pTemp) + addValue, 2)
            if pTemp > float(self.Temp_input_3.text()):
                pTemp = round(float(pTemp) - addValue, 2)

        else:
            pTemp = round(float(pTemp) + addValue, 2)
            if pTemp < float(self.Temp_input_3.text()):
                pTemp = round(float(pTemp) - addValue, 2)

        pTemp = str(pTemp)
        self.Temp_input_2.setText(pTemp)
        config.set('Section1', 'temp', pTemp)

        # RH

        addValue = int(self.RH_input_4.text())
        if addValue > 0:
            pRH = int(float(pRH)) + addValue
            if pRH > int(self.RH_input_3.text()):
                pRH = int(pRH) - addValue

        else:
            pRH = int(float(pRH)) + addValue
            if pRH < int(self.RH_input_3.text()):
                pRH = int(pRH) - addValue

        pRH = str(pRH)
        self.RH_input_2.setText(pRH)
        config.set('Section1', 'RH', pRH)

        # PM2p5

        addValue = int(self.PM2p5_input_4.text())
        if addValue > 0:
            pPM2p5 = int(float(pPM2p5)) + addValue
            if pPM2p5 > int(self.PM2p5_input_3.text()):
                pPM2p5 = int(pPM2p5) - addValue

        else:
            pPM2p5 = int(float(pPM2p5)) + addValue
            if pPM2p5 < int(self.PM2p5_input_3.text()):
                pPM2p5 = int(pPM2p5) - addValue

        pPM2p5 = str(pPM2p5)
        self.PM2p5_input_2.setText(pPM2p5)
        config.set('Section1', 'PM2.5', pPM2p5)

        # PM10

        addValue = int(self.PM10_input_4.text())
        if addValue > 0:
            pPM10 = int(float(pPM10)) + addValue
            if pPM10 > int(self.PM10_input_3.text()):
                pPM10 = int(pPM10) - addValue

        else:
            pPM10 = int(float(pPM10)) + addValue
            if pPM10 < int(self.PM10_input_3.text()):
                pPM10 = int(pPM10) - addValue

        pPM10 = str(pPM10)
        self.PM10_input_2.setText(pPM10)
        config.set('Section1', 'PM10', pPM10)

        # O3

        addValue = float(self.O3_input_4.text())
        if addValue > 0:
            pO3 = round(float(pO3) + addValue, 2)
            if pO3 > float(self.O3_input_3.text()):
                pO3 = round(float(pO3) - addValue, 2)

        else:
            pO3 = round(float(pO3) + addValue, 2)
            if pO3 < float(self.O3_input_3.text()):
                pO3 = round(float(pO3) - addValue, 2)

        pO3 = str(pO3)
        self.O3_input_2.setText(pO3)
        config.set('Section1', 'O3', pO3)

        # CO

        addValue = int(self.CO_input_4.text())
        if addValue > 0:
            pCO = int(float(pCO)) + addValue
            if pCO > int(self.CO_input_3.text()):
                pCO = int(pCO) - addValue

        else:
            pCO = int(float(pCO)) + addValue
            if pCO < int(self.CO_input_3.text()):
                pCO = int(pCO) - addValue

        pCO = str(pCO)
        self.CO_input_2.setText(pCO)
        config.set('Section1', 'CO', pCO)

        # CO2

        addValue = int(self.CO2_input_4.text())
        if addValue > 0:
            pCO2 = int(float(pCO2)) + addValue
            if pCO2 > int(self.CO2_input_3.text()):
                pCO2 = int(pCO2) - addValue

        else:
            pCO2 = int(float(pCO2)) + addValue
            if pCO2 < int(self.CO2_input_3.text()):
                pCO2 = int(pCO2) - addValue

        pCO2 = str(pCO2)
        self.CO2_input_2.setText(pCO2)
        config.set('Section1', 'CO2', pCO2)

        # TVOC

        addValue = int(self.TVOC_input_4.text())
        if addValue > 0:
            pTVOC = int(float(pTVOC)) + addValue
            if pTVOC > int(self.TVOC_input_3.text()):
                pTVOC = int(pTVOC) - addValue

        else:
            pTVOC = int(float(pTVOC)) + addValue
            if pTVOC < int(self.TVOC_input_3.text()):
                pTVOC = int(pTVOC) - addValue

        pTVOC = str(pTVOC)
        self.TVOC_input_2.setText(pTVOC)
        config.set('Section1', 'CO2', pTVOC)

        # CH2O

        addValue = float(self.CH2O_input_4.text())
        if addValue > 0:
            pCH2O = round(float(pCH2O) + addValue, 3)
            if pCH2O > float(self.CH2O_input_3.text()):
                pCH2O = round(float(pCH2O) - addValue, 3)

        else:
            pCH2O = round(float(pCH2O) + addValue, 3)
            if pCH2O < float(self.CH2O_input_3.text()):
                pCH2O = round(float(pCH2O) - addValue, 3)

        pCH2O = str(pCH2O)
        self.CH2O_input_2.setText(pCH2O)
        config.set('Section1', 'O3', pCH2O)

        with open('example.cfg', 'w') as configfile:
            config.write(configfile)

            # {A8:03:2A:57:0C:CC_DEV} b'{"CMD":0,"srReadMode":1,"IdNum":19616,"Temp":-5535,"RH":60001,"PM2p5":3,"PM10":3,"O3":0.01,"CO":0,"CO2":803,"TVOC":867,"CH2O":0.507,"NO2":65535}
        return

    def _poll_console_queue(self):
        """Write any queued console text to the console text area from the main thread."""
        while not self.console_queue.empty():
            string = str(self.console_queue.get())
            stripped = string.rstrip()
            if stripped != "":
                self.consoleOutput.appendPlainText(stripped)
        return


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
