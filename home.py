import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget, QSpacerItem, QSizePolicy, QSlider, QStackedWidget
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.widgets import SliderBase
from fnirs_slider import MainWindow
from NIRS_topo_slider import TopoMainWindow

from screenshot_eye_track_slider import Window
from screenshot_eye_track_slider import Window as WindowEEG


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the position and size of the widget
        self.setGeometry(200, 200, 400, 300)

        view_Label = QLabel("")
        slider = QSlider(Qt.Horizontal, self)
        slider.setTickInterval(1)

        window = Window()
        signal_fNIRS = MainWindow()
        signal_EEG = WindowEEG()
        topo_fNIRS = TopoMainWindow()

        slider.setMinimum(0)
        slider.setMaximum(50)
        slider.setGeometry(200, 2000, 100, 20)
        slider.setRange(0, 49)
        slider.valueChanged.connect(window.load_image)
        slider.valueChanged.connect(signal_fNIRS.update_plot_data)
        slider.valueChanged.connect(topo_fNIRS.slider_moved)
        slider.setTickPosition(QSlider.TicksBelow)

        slider_text = QLabel(self)
        slider_text.setGeometry(200, 850, 150, 20)

        # Add a border style to each label
        view_Label.setStyleSheet("border: 1px solid black;")
        slider.setStyleSheet("border: 1px solid black;")

        # Set custom dimensions for each label
        # label1.setFixedSize(1500, 1000)
        # label2.setFixedSize(300, 700)
        # label3.setFixedSize(200, 90)
        view_Label.setFixedSize(300, 90)
        slider.setFixedSize(1400, 50)

        # Create the layout managers
        main_layout = QVBoxLayout()

        # create the first row layout which includes eye-tracking and signal view
        sub_layout1 = QHBoxLayout()
        eye_tracking = QVBoxLayout()
        fNIRS_EEG = QVBoxLayout()
        buttons = QVBoxLayout()

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

        # Create the stacked widget for the views in Box 2
        stacked_widget = QStackedWidget()

        # Create the first view (View 1) and add it to the stacked widget
        stacked_widget.addWidget(signal_fNIRS)

        # Create the first view (View 1) and add it to the stacked widget
        stacked_widget.addWidget(signal_EEG)

        # Create the second view (View 2) and add it to the stacked widget
        stacked_widget.addWidget(topo_fNIRS)

        # Create the second view (View 2) and add it to the stacked widget
        view2 = QLabel("View 2 EEG Topological")
        view2.setStyleSheet("border: 1px solid black;")
        stacked_widget.addWidget(view2)

        def switchButton1View():
            button1_property = button.property("value")
            button2_property = buttonView.property("value")
            print("Button1: ", button1_property, button2_property)
            if button1_property == "fNIRS":
                button.setProperty("value", "EEG")
                if button2_property == "signal":
                    stacked_widget.setCurrentIndex(1)
                elif button2_property == "topological":
                    stacked_widget.setCurrentIndex(3)
            elif button1_property == "EEG":
                button.setProperty("value", "fNIRS")
                if button2_property == "signal":
                    stacked_widget.setCurrentIndex(0)
                elif button2_property == "topological":
                    stacked_widget.setCurrentIndex(2)

        def switchButton2View():
            button1_property = button.property("value")
            button2_property = buttonView.property("value")
            print("Button2: ", button1_property, button2_property)
            if button2_property == "signal":
                buttonView.setProperty("value", "topological")
                if button1_property == "fNIRS":
                    stacked_widget.setCurrentIndex(2)
                elif button1_property == "EEG":
                    stacked_widget.setCurrentIndex(3)
            elif button2_property == "topological":
                buttonView.setProperty("value", "signal")
                if button1_property == "fNIRS":
                    stacked_widget.setCurrentIndex(0)
                elif button1_property == "EEG":
                    stacked_widget.setCurrentIndex(1)

        # Create a button
        button = QPushButton('fNIRS or EEG', self)
        # Set the property of button1 to indicate its value
        button.setProperty("value", "fNIRS")

        # Connect the button's clicked signal to a function
        button.clicked.connect(switchButton1View)

        # Create a button
        buttonView = QPushButton('Signal or Topological View', self)
        # Set the property of button2 to indicate its value
        buttonView.setProperty("value", "signal")

        # Connect the button's clicked signal to a function
        buttonView.clicked.connect(switchButton2View)

        # Add the labels to the respective layouts
        eye_tracking.addWidget(window)
        fNIRS_EEG.addWidget(button)
        fNIRS_EEG.addWidget(stacked_widget)
        fNIRS_EEG.addWidget(buttonView)

        # buttons.addWidget(button)
        # buttons.addWidget(buttonView)

        slider_box.addWidget(slider)

        self.setLayout(main_layout)

        self.show()  # Show the widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
