from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from utils import read_screenshots

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "ToMCAT offline viz"
        self.top = 200
        self.left = 500
        self.width = 1400
        self.height = 1300

        self.InitWindow()

    
    def InitWindow(self):
        hbox = QHBoxLayout()
        min, max, self.screenshots = read_screenshots()
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(self.screenshots[0]))
        self.label.setGeometry(60, 60, 1280, 720)
        
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setTickInterval(1)

        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setGeometry(100, 830, 1000, 20)
        self.slider.valueChanged[int].connect(self.changedValue)
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.setLayout(hbox)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def changedValue(self, value):
        # change value of the slider when you move the slider and switch to the next img
        self.label.setPixmap(QPixmap(self.screenshots[value]))
        print(self.screenshots[value])
        # size = self.slider.value()
        # self.label.setText(str(size))

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())