import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget, QSpacerItem, QSizePolicy, QSlider
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.widgets import SliderBase

from screenshot_eye_track_slider import Window


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 300)  # Set the position and size of the widget

        label1 = QLabel("eye-tracking")
        label2 = QLabel("fNIRS")
        label3 = QLabel("Button to switch")
        label4 = QLabel("Slider")

        # Add a border style to each label
        label1.setStyleSheet("border: 1px solid black;")
        label2.setStyleSheet("border: 1px solid black;")
        label3.setStyleSheet("border: 1px solid black;")
        label4.setStyleSheet("border: 1px solid black;")

        # Set custom dimensions for each label
        label1.setFixedSize(1100, 800)
        label2.setFixedSize(300, 700)
        label3.setFixedSize(200, 90)
        label4.setFixedSize(1400, 50)

        # Create the layout managers
        main_layout = QVBoxLayout()

        # create the first row layout which includes eye-tracking and signal view
        sub_layout1 = QHBoxLayout()
        eye_tracking = QVBoxLayout()
        fNIRS_EEG = QVBoxLayout()

        # Set the stretch factor for the main layout to make box 1 take 2/3 of the vertical space
        main_layout.addLayout(sub_layout1)

        # Set the stretch factor for box 2 and box 3 to divide the remaining vertical space equally
        sub_layout1.addLayout(eye_tracking, 2)
        sub_layout1.addLayout(fNIRS_EEG)

        # Create the second row layout
        sub_layout2 = QHBoxLayout()
        slider = QVBoxLayout()

        # Set the stretch factor for the second row layout to divide the vertical space equally
        main_layout.addLayout(sub_layout2)

        # Set the stretch factor for box 1 in the second row layout to make it 2/3 of the row's width
        sub_layout2.addLayout(slider, 2)

        window = Window()

        # Add the labels to the respective layouts
        eye_tracking.addWidget(window)
        fNIRS_EEG.addWidget(label2)
        fNIRS_EEG.addWidget(label3)
        slider.addWidget(label4)
        
        # self.button = QPushButton('Click me', self)  
        # Create a button

        # vbox.addWidget(self.button)
        # self.button.clicked.connect(self.on_button_clicked)  # Connect the button's clicked signal to a function

        # self.label = QLabel(self)  # Create a label
        # self.label.setText('Button not clicked yet')  # Set the initial text for the label
        # self.label.move(10, 50)  # Move the label to a specific position

        self.setLayout(main_layout)

        self.show()  # Show the widget

    # def on_button_clicked(self):
    #     self.label.setText('Button clicked')  # Update the label's text when the button is clicked


    # def changedValue(self, value):
    #     # change value of the slider when you move the slider and switch to the next img
    #     start = time.process_time()

    #     rgb_image = cv2.cvtColor(self.screenshots[value], cv2.COLOR_BGR2RGB)
    #     # print(self.x[value], self.y[value])
    #     x_value = self.x.get(value, None)
    #     y_value = self.y.get(value, None)

    #     if x_value is not None and y_value is not None:
    #         cv2.circle(rgb_image, (int(x_value), int(y_value)),
    #                    5, (255, 0, 0), 2)

    #     h, w, ch = rgb_image.shape
    #     bytes_per_line = ch * w
    #     convert_to_Qt_format = QtGui.QImage(
    #         rgb_image, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    #     self.ScreenShot.setPixmap(QPixmap.fromImage(convert_to_Qt_format))

    #     val = self.slider.value()
    #     self.slider_text.setText(str(val))
    #     print('Time taken by changedValue:', time.process_time() - start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
