import matplotlib.pyplot as plt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from utils import read_screenshots, read_pupil_data
import time
import cv2
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QTextEdit, QPushButton

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
        min, max, self.screenshots = read_screenshots()
        print(min, max)

        self.x, self.y, point_scale, id_labels = read_pupil_data()

        hbox = QHBoxLayout()

        # Create a vertical layout for the button
        vbox = QVBoxLayout()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setTickInterval(1)

        # create the tab widget and add it to the layout
        self.tab_widget = QTabWidget()
        vbox.addWidget(self.tab_widget)

        self.slider.setMinimum(min)
        self.slider.setMaximum(max)
        self.slider.setGeometry(150, 80, 1000, 20)
        self.slider.sliderMoved[int].connect(self.changedValue)
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.slider_text = QLabel(self)
        self.tab_widget.addTab(self.slider_text, "Subject-1")
        self.slider_text.setGeometry(100, 860, 900, 20)

        self.ScreenShot = QLabel(self)
        # self.ScreenShot.setPixmap(QPixmap(self.screenshots[0]))
        self.ScreenShot.setGeometry(60, 60, 1280, 720)

        # Add the slider to the vertical layout
        vbox.addWidget(self.slider)
        # Add the vertical layout to the horizontal layout
        hbox.addLayout(vbox)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.tab2 = QPushButton("Click me")
        self.tab_widget.addTab(self.tab2, "Subject-2")

        self.setLayout(hbox)
        # self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()

    def changedValue(self, value):
        # change value of the slider when you move the slider and switch to the next img
        start = time.process_time()

        rgb_image = cv2.cvtColor(self.screenshots[value], cv2.COLOR_BGR2RGB)
        # print(self.x[value], self.y[value])
        x_value = self.x.get(value, None)
        y_value = self.y.get(value, None)

        if x_value is not None and y_value is not None:
            cv2.circle(rgb_image, (int(x_value), int(y_value)), 5, (255, 0, 0), 2)

        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        self.ScreenShot.setPixmap(QPixmap.fromImage(convert_to_Qt_format))

        val = self.slider.value()
        self.slider_text.setText(str(val))
        print('Time taken by changedValue:', time.process_time() - start)
            

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
