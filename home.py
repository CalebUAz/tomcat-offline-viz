import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget, QSpacerItem, QSizePolicy, QSlider
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.widgets import SliderBase
from fnirs_slider import MainWindow

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
        slider = QSlider(Qt.Horizontal, self)
        slider.setTickInterval(1)

        window = Window()
        signal = MainWindow()

        slider.setMinimum(0)
        slider.setMaximum(50)
        slider.setGeometry(200, 2000, 100, 20)
        slider.setRange(0, 999)
        slider.valueChanged.connect(window.load_image)
        # slider.sliderMoved[int].connect(window.changedValue)
        slider.valueChanged.connect(signal.update_plot_data)
        slider.setTickPosition(QSlider.TicksBelow)

        slider_text = QLabel(self)
        slider_text.setGeometry(200, 850, 150, 20)

        # Add a border style to each label
        label1.setStyleSheet("border: 1px solid black;")
        label2.setStyleSheet("border: 1px solid black;")
        label3.setStyleSheet("border: 1px solid black;")
        slider.setStyleSheet("border: 1px solid black;")

        # Set custom dimensions for each label
        label1.setFixedSize(1500, 1000)
        label2.setFixedSize(300, 700)
        label3.setFixedSize(200, 90)
        slider.setFixedSize(1400, 50)

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
        slider_box = QVBoxLayout()

        # Set the stretch factor for the second row layout to divide the vertical space equally
        main_layout.addLayout(sub_layout2)

        # Set the stretch factor for box 1 in the second row layout to make it 2/3 of the row's width
        sub_layout2.addLayout(slider_box)

        # Add the labels to the respective layouts
        eye_tracking.addWidget(window)
        fNIRS_EEG.addWidget(signal)
        fNIRS_EEG.addWidget(label3)
        slider_box.addWidget(slider)
        
        # button = QPushButton('Click me', self)  
        # Create a button

        # vbox.addWidget(button)
        # button.clicked.connect(on_button_clicked)  # Connect the button's clicked signal to a function

        # label = QLabel(self)  # Create a label
        # label.setText('Button not clicked yet')  # Set the initial text for the label
        # label.move(10, 50)  # Move the label to a specific position

        self.setLayout(main_layout)

        self.show()  # Show the widget

    # def on_button_clicked(self):
    #     self.label.setText('Button clicked')  # Update the label's text when the button is clicked

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
