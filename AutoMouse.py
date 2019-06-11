#PyQt
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
# 마우스/ 키보드
from pynput import mouse, keyboard

import threading
import time

main_window_ui = uic.loadUiType('MainWindow3.ui')[0]

class MainWindow(QMainWindow, main_window_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CMouse = mouse.Controller()
        self.StartKey = keyboard.Key.f9
        self.EndKey = keyboard.Key.f12
        self.ButtonRL = mouse.Button.left
        self.NOP = 2
        self.KeySetStart.activated[str].connect(self.SetKey1)
        self.KeySetEnd.activated[str].connect(self.SetKey2)
        self.LeftButton.toggled.connect(self.ToggledSetMouse1)
        self.RightButton.toggled.connect(self.ToggledSetMouse2)
        self.PlusButton.clicked.connect(self.PlusSetting)
        self.ThreadStart()

    def StartSetting(self):
        if self.StartKey == self.EndKey:return 0
        try:
            self.EndFlag = 1
            self.ClickT = int(self.ClickTime.text())
        except:
            return 0
        try:
            self.X1 = int(self.X_AxisValue_2.text())
            self.Y1 = int(self.Y_AxisValue_2.text())
        except:
            self.Start0Position()
        try:
            self.X2 = int(self.X_AxisValue_3.text())
            self.Y2 = int(self.Y_AxisValue_3.text())
        except:
            self.Start1Position()
        try:
            self.X3 = int(self.X_AxisValue_n.text())
            self.Y3 = int(self.Y_AxisValue_n.text())
        except:
            self.Start2Position()
        self.Start3Position()
    def Start0Position(self):
        while self.EndFlag == 1:
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
    def Start1Position(self):
        while self.EndFlag == 1:
            self.CMouse.position = (self.X1, self.Y1)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
    def Start2Position(self):
        while self.EndFlag == 1:
            self.CMouse.position = (self.X1, self.Y1)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
            self.CMouse.position = (self.X2, self.Y2)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
    def Start3Position(self):
        while self.EndFlag == 1:
            self.CMouse.position = (self.X1, self.Y1)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
            self.CMouse.position = (self.X2, self.Y2)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)
            self.CMouse.position = (self.X3, self.Y3)
            self.CMouse.click(self.ButtonRL, 1)
            time.sleep(1/self.ClickT)

    def SetKey1(self, text):
        key = {"F1":keyboard.Key.f1, "F2":keyboard.Key.f2, "F4":keyboard.Key.f4,
            "F5":keyboard.Key.f5, "F6":keyboard.Key.f6, "F9":keyboard.Key.f9,
            "F12":keyboard.Key.f12, "ESC":keyboard.Key.esc}
        self.StartKey = key[text]
    def SetKey2(self, text):
        key = {"F1":keyboard.Key.f1, "F2":keyboard.Key.f2, "F4":keyboard.Key.f4,
            "F5":keyboard.Key.f5, "F6":keyboard.Key.f6, "F9":keyboard.Key.f9,
            "F12":keyboard.Key.f12, "ESC":keyboard.Key.esc}
        self.EndKey = key[text]

    def ToggledSetMouse1(self):
        self.RightButton.setChecked(False)
        self.ButtonRL = mouse.Button.left
    def ToggledSetMouse2(self):
        self.LeftButton.setChecked(False)
        self.ButtonRL = mouse.Button.right

    def PlusSetting(self):
        if self.NOP == 3: return 0
        self.X_Axis_n = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.X_Axis_n.setText("X :")
        self.X_AxisValue_n = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Y_Axis_n = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Y_Axis_n.setText("Y :")
        self.Y_AxisValue_n = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.X_Axis_n, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.X_AxisValue_n, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.Y_Axis_n, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.Y_AxisValue_n, 2, 4, 1, 1)
        self.NOP += 1
        self.MinusButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.MinusButton.setText("-")
        self.gridLayout_2.addWidget(self.MinusButton, 2, 0, 1, 1)
        self.MinusButton.clicked.connect(self.MinusSetting)

    def MinusSetting(self):
        self.gridLayout_2.removeWidget(self.X_Axis_n)
        self.gridLayout_2.removeWidget(self.Y_Axis_n)
        self.gridLayout_2.removeWidget(self.X_AxisValue_n)
        self.gridLayout_2.removeWidget(self.Y_AxisValue_n)
        self.gridLayout_2.removeWidget(self.MinusButton)
        self.X_Axis_n.deleteLater()
        self.Y_Axis_n.deleteLater()
        self.X_AxisValue_n.deleteLater()
        self.Y_AxisValue_n.deleteLater()
        self.MinusButton.deleteLater()
        self.X_Axis_n = None
        self.Y_Axis_n = None
        self.X_AxisValue_n = None
        self.Y_AxisValue_n = None
        self.MinusButton = None
        self.NOP -= 1
        
    def ThreadStart(self):
        self.th1 = threading.Thread(target = self.MousePosition)
        self.th2 = threading.Thread(target = self.KeyboardListen)
        self.th1.daemon = True
        self.th2.daemon = True
        self.th1.start()
        self.th2.start()

    def MousePosition(self):
        def on_move(x, y):
            self.X_AxisValue.setText("%.0f"%(x))
            self.Y_AxisValue.setText("%.0f"%(y))
            self.X_Po = x
            self.Y_Po = y
        with mouse.Listener(on_move = on_move) as Mlistener:
            Mlistener.join()

    def KeyboardListen(self):
        def on_press(key):
            if key == keyboard.Key.f7:
                self.X_AxisValue_2.setText("%.0f"%(self.X_Po))
                self.Y_AxisValue_2.setText("%.0f"%(self.Y_Po))
            elif key == keyboard.Key.f8:
                self.X_AxisValue_3.setText("%.0f"%(self.X_Po))
                self.Y_AxisValue_3.setText("%.0f"%(self.Y_Po))
            elif key == self.StartKey:
                self.th3 = threading.Thread(target = self.StartSetting)
                self.th3.daemon = True
                self.th3.start()
            elif key == self.EndKey:
                self.EndFlag = 0
        with keyboard.Listener(on_press = on_press) as Klistener:
            Klistener.join()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
