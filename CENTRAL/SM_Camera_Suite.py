#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
import socket
import time
# from signal import signal, SIGPIPE, SIG_DFL
import threading
import sys
import cv2
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
import datetime
import pickle
import numpy as np
import json
from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxState:

    def __init__(self) -> None:
        self.box1_val = 60
        self.box2_val = 60
        self.box3_val = 60
        self.box4_val = 60

    def updateVals(self, val1, val2, val3, val4):
        self.box1_val = int(val1)
        self.box2_val = int(val2)
        self.box3_val = int(val3)
        self.box4_val = int(val4)

    # Function to return a str object of the class details
    def getParams(self):
        class_dict = self.__dict__
        return class_dict


class Ui_Form(object):

    def constructor_func(self):
        self.th_setCameraImageLabel1 = threading.Thread(
            target=self.getCameraImage1)
        self.th_setCameraImageLabel2 = threading.Thread(
            target=self.getCameraImage2)
        self.th_setCameraImageLabel3 = threading.Thread(
            target=self.getCameraImage3)
        self.th_setCameraImageLabel4 = threading.Thread(
            target=self.getCameraImage4)
        self.th_ComboBoxThread = threading.Thread(target=self.send_params)
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.comboxobj = ComboBoxState()

    def create_gui_elements(self, Form):
        self.constructor_func()
        Form.setObjectName("Form")
        Form.resize(1388, 873)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(230, 70, 71, 17))
        self.label_8.setObjectName("label_8")
        self.Camera4Label = QtWidgets.QLabel(Form)
        self.Camera4Label.setGeometry(QtCore.QRect(710, 510, 651, 341))
        self.Camera4Label.setAutoFillBackground(True)
        self.Camera4Label.setObjectName("Camera4Label")
        self.comboBoxCam3 = QtWidgets.QComboBox(Form)
        self.comboBoxCam3.setGeometry(QtCore.QRect(350, 90, 86, 25))
        self.comboBoxCam3.setObjectName("comboBoxCam3")
        self.comboBoxCam3.addItem("")
        self.comboBoxCam3.addItem("")
        self.comboBoxCam3.addItem("")
        self.comboBoxCam3.addItem("")
        self.comboBoxCam3.addItem("")
        self.comboBoxCam3.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Camera3Label = QtWidgets.QLabel(Form)
        self.Camera3Label.setGeometry(QtCore.QRect(30, 510, 651, 341))
        self.Camera3Label.setAutoFillBackground(True)
        self.Camera3Label.setObjectName("Camera3Label")
        self.comboBoxCam2 = QtWidgets.QComboBox(Form)
        self.comboBoxCam2.setGeometry(QtCore.QRect(220, 90, 86, 25))
        self.comboBoxCam2.setObjectName("comboBoxCam2")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam2.addItem("")
        self.comboBoxCam1 = QtWidgets.QComboBox(Form)
        self.comboBoxCam1.setGeometry(QtCore.QRect(80, 90, 86, 25))
        self.comboBoxCam1.setObjectName("comboBoxCam1")
        self.comboBoxCam1.addItem("")
        self.comboBoxCam1.addItem("")
        self.comboBoxCam1.addItem("")
        self.comboBoxCam1.addItem("")
        self.comboBoxCam1.addItem("")
        self.comboBoxCam1.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 70, 71, 17))
        self.label_7.setObjectName("label_7")
        self.Camera1Label = QtWidgets.QLabel(Form)
        self.Camera1Label.setGeometry(QtCore.QRect(30, 150, 651, 341))
        self.Camera1Label.setAutoFillBackground(True)
        self.Camera1Label.setObjectName("Camera1Label")
        self.Camera2Label = QtWidgets.QLabel(Form)
        self.Camera2Label.setGeometry(QtCore.QRect(710, 150, 651, 341))
        self.Camera2Label.setAutoFillBackground(True)
        self.Camera2Label.setObjectName("Camera2Label")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 31, 17))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(360, 70, 71, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(500, 70, 71, 17))
        self.label_10.setObjectName("label_10")
        self.comboBoxCam4 = QtWidgets.QComboBox(Form)
        self.comboBoxCam4.setGeometry(QtCore.QRect(490, 90, 86, 25))
        self.comboBoxCam4.setObjectName("comboBoxCam4")
        self.comboBoxCam4.addItem("")
        self.comboBoxCam4.addItem("")
        self.comboBoxCam4.addItem("")
        self.comboBoxCam4.addItem("")
        self.comboBoxCam4.addItem("")
        self.comboBoxCam4.addItem("")
        self.showImage_btn = QtWidgets.QPushButton(Form)
        self.showImage_btn.setGeometry(QtCore.QRect(460, 20, 89, 25))
        self.showImage_btn.setAutoFillBackground(True)
        self.showImage_btn.setObjectName("showImage_btn")
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(1280, 20, 101, 25))
        self.close_btn.setObjectName("close_btn")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Camera 2"))
        self.Camera4Label.setText(_translate("Form", "Image4"))
        self.comboBoxCam3.setItemText(0, _translate("Form", "1"))
        self.comboBoxCam3.setItemText(1, _translate("Form", "5"))
        self.comboBoxCam3.setItemText(2, _translate("Form", "10"))
        self.comboBoxCam3.setItemText(3, _translate("Form", "20"))
        self.comboBoxCam3.setItemText(4, _translate("Form", "30"))
        self.comboBoxCam3.setItemText(5, _translate("Form", "60"))
        self.comboBoxCam3.setCurrentText("60")
        self.label_5.setText(_translate("Form", "ROBOTIC ARM IMAGE SUITE"))
        self.Camera3Label.setText(_translate("Form", "Image3"))
        self.comboBoxCam2.setItemText(0, _translate("Form", "1"))
        self.comboBoxCam2.setItemText(1, _translate("Form", "5"))
        self.comboBoxCam2.setItemText(2, _translate("Form", "10"))
        self.comboBoxCam2.setItemText(3, _translate("Form", "20"))
        self.comboBoxCam2.setItemText(4, _translate("Form", "30"))
        self.comboBoxCam2.setItemText(5, _translate("Form", "60"))
        self.comboBoxCam2.setCurrentText("60")
        self.comboBoxCam1.setItemText(0, _translate("Form", "1"))
        self.comboBoxCam1.setItemText(1, _translate("Form", "5"))
        self.comboBoxCam1.setItemText(2, _translate("Form", "10"))
        self.comboBoxCam1.setItemText(3, _translate("Form", "20"))
        self.comboBoxCam1.setItemText(4, _translate("Form", "30"))
        self.comboBoxCam1.setItemText(5, _translate("Form", "60"))
        self.comboBoxCam1.setCurrentText("60")
        self.label_7.setText(_translate("Form", "Camera 1"))
        self.Camera1Label.setText(_translate("Form", "Image1"))
        self.Camera2Label.setText(_translate("Form", "Image2"))
        self.label_6.setText(_translate("Form", "FPS"))
        self.label_9.setText(_translate("Form", "Camera 3"))
        self.label_10.setText(_translate("Form", "Camera 4"))
        self.showImage_btn.setText(_translate("Form", "Show Image"))
        self.close_btn.setText(_translate("Form", "Close"))
        self.comboBoxCam4.setItemText(0, _translate("Form", "1"))
        self.comboBoxCam4.setItemText(1, _translate("Form", "5"))
        self.comboBoxCam4.setItemText(2, _translate("Form", "10"))
        self.comboBoxCam4.setItemText(3, _translate("Form", "20"))
        self.comboBoxCam4.setItemText(4, _translate("Form", "30"))
        self.comboBoxCam4.setItemText(5, _translate("Form", "60"))
        self.comboBoxCam4.setCurrentText("60")
        self.gui_buttonevents()

    def getCameraUDP(self, host, port, label):
        max_length = 65540
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        frame_info = None
        buffer = None
        frame = None
        print("-> waiting for connection")
        while True:
            data, address = sock.recvfrom(max_length)
            if len(data) < 100:
                frame_info = pickle.loads(data)

                if frame_info:
                    nums_of_packs = frame_info["packs"]

                    for i in range(nums_of_packs):
                        data, address = sock.recvfrom(max_length)

                        if i == 0:
                            buffer = data
                        else:
                            buffer += data

                    frame = np.frombuffer(buffer, dtype=np.uint8)
                    frame = frame.reshape(frame.shape[0], 1)

                    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                    frame = cv2.flip(frame, 1)

                    if frame is not None and type(frame) == np.ndarray:
                        cv_img = frame
                        qt_img = self.convert_cv_qt(cv_img, 791, 571)
                        label.setPixmap(qt_img)

    def setupUi(self, Form):
        self.create_gui_elements(Form)

    # Convert from an opencv image to QPixmap
    def convert_cv_qt(self, cv_img, width, hieght):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, hieght, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def send_params(self):
        # binding port and host
        self.s1.bind(("127.0.0.1", 12368))
        print("Waiting for client to connect")
        # waiting for a client to connect
        self.s1.listen(5)
        c, addr = self.s1.accept()
        while True:
            self.data_packet_msg = self.comboxobj.getParams()
            self.data_packet_msg = json.dumps(self.data_packet_msg)
            print("Sent msg {}".format(self.data_packet_msg))
            c.send(self.data_packet_msg.encode())
            time.sleep(5)

    def getCameraImage1(self):
        self.getCameraUDP("127.0.0.1", 12362, self.Camera1Label)

    def getCameraImage2(self):
        self.getCameraUDP("127.0.0.1", 12363, self.Camera2Label)

    def getCameraImage3(self):
        self.getCameraUDP("127.0.0.1", 12364, self.Camera3Label)

    def getCameraImage4(self):
        self.getCameraUDP("127.0.0.1", 12365, self.Camera4Label)

    def gui_buttonevents(self):
        self.showImage_btn.clicked.connect(self.Display_Image_function)
        self.close_btn.clicked.connect(self.exit_gui)
        self.comboBoxCam1.currentIndexChanged.connect(
            self.onComboBoxValueChange)
        self.comboBoxCam2.currentIndexChanged.connect(
            self.onComboBoxValueChange)
        self.comboBoxCam3.currentIndexChanged.connect(
            self.onComboBoxValueChange)
        self.comboBoxCam4.currentIndexChanged.connect(
            self.onComboBoxValueChange)

    def Display_Image_function(self):
        self.th_setCameraImageLabel1.start()
        time.sleep(0.3)
        self.th_setCameraImageLabel2.start()
        time.sleep(0.3)
        self.th_setCameraImageLabel3.start()
        time.sleep(0.3)
        self.th_setCameraImageLabel4.start()
        time.sleep(0.1)
        self.th_ComboBoxThread.start()

    def onComboBoxValueChange(self):
        self.comboxobj.updateVals(self.comboBoxCam1.currentText(), self.comboBoxCam2.currentText(
        ), self.comboBoxCam3.currentText(), self.comboBoxCam4.currentText())

    def exit_gui(self):
        self.th_setCameraImageLabel1.join()
        self.th_setCameraImageLabel2.join()
        self.th_setCameraImageLabel3.join()
        self.th_setCameraImageLabel4.join()
        self.th_ComboBoxThread.join()
        print("Cleaning Up and Exiting...")
        time.sleep(3)
        sys.exit(0)


def startGUI():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        startGUI()
    except KeyboardInterrupt:
        print("Shutting Down Program")
        sys.exit(0)
