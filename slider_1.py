from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from utils import read_screenshots

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Slider"
        self.top = 200
        self.left = 500
        self.width = 1400
        self.height = 1300

        self.InitWindow()
    
    def InitWindow(self):
        # hbox = QHBoxLayout()

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output000011.png'))
        self.label.setGeometry(60, 60, 1280, 720)
        
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setGeometry(100, 830, 1000, 20)
        self.slider.valueChanged[int].connect(self.changedValue)
        # self.slider.setTickPosition(QSlider.TicksBelow)
        # self.label = QLabel("0")

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        # self.setLayout(hbox)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

        # # self.setWindowIcon(QtGui.QIcon("icon.png"))
        # # self.setWindowTitle(self.title)
        # hbox = QHBoxLayout()


        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output000011.png'))
        # self.label.setGeometry(60, 60, 1280, 720)

        # self.slider = QSlider(Qt.Horizontal, self)
        # self.slider.setGeometry(100, 60, 1340, 20)
        # self.slider.valueChanged[int].connect(self.changedValue)
                
        # self.slider.setTickPosition(QSlider.TicksBelow)
        # self.slider.setTickInterval(1)
        # self.slider.setMinimum(0)
        # self.slider.setMaximum(100)
        # self.label = QLabel("0")
        # # self.label.setFont(QtGui.QFont("Sanserif", 15))
        # hbox.addWidget(self.slider)
        # hbox.addWidget(self.label)
        # self.setLayout(hbox)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # self.show()

    def changedValue(self, value):
        # change value of the slider when you move the slider and switch to the next img
        if value == 0:
            # print(value)
            self.label.setPixmap(QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output033301.png'))
        elif value < 50:
            # print(value)
            self.label.setPixmap(QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output054237.png'))
        else:
            # print(value)
            self.label.setPixmap(QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064216.png'))

        # size = self.slider.value()
        # self.label.setText(str(size))

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())