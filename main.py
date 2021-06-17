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


mqtt_rc_codes = ['Success', 'Incorrect protocol version', 'Invalid client identifier', 'Server unavailable', 'Bad username or password', 'Not authorized']

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
        self.RH_input_2.setText(config.get('Section1', 'rh', raw=False))
        self.PM2p5_input_2.setText(config.get('Section1', 'pm2.5', raw=False))
        self.PM10_input_2.setText(config.get('Section1', 'pm10', raw=False))
        self.O3_input_2.setText(config.get('Section1', 'o3', raw=False))
        self.CO_input_2.setText(config.get('Section1', 'co', raw=False))
        self.CO2_input_2.setText(config.get('Section1', 'co2', raw=False))
        self.TVOC_input_2.setText(config.get('Section1', 'tvoc', raw=False))
        self.CH2O_input_2.setText(config.get('Section1', 'hcho', raw=False))


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
        print("Hello2")

        if self.client.is_connected():
            self.client.publish("Sam_Test", "Sam_Hello")
        else:
            self.window.write("Not connected.")

            {A8: 03: 2
            A: 57:0
            C: CC_DEV} b'{"CMD":0,"srReadMode":1,"IdNum":19616,"Temp":-5535,"RH":60001,"PM2p5":3,"PM10":3,"O3":0.01,"CO":0,"CO2":803,"TVOC":867,"CH2O":0.507,"NO2":65535}
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
