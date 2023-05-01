import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget, QSpacerItem, QSizePolicy, QSlider, QStackedWidget, QFrame
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QColor
from matplotlib.widgets import SliderBase

from fnirs_slider import MainWindow
from NIRS_topo_slider import TopoMainWindow

from screenshot_eye_track_slider import Window

from EEG_slider import MainWindow as WindowEEG
from EEG_topo_slider import TopoMainWindow as TopoMainWindowEEG


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Get the screen resolution
        screen_resolution = QApplication.desktop().screenGeometry()

        # Calculate the desired position and size based on screen resolution
        x = int(screen_resolution.width() * 0.1)
        y = int(screen_resolution.height() * 0.1)
        width = int(screen_resolution.width() * 0.9)
        height = int(screen_resolution.height() * 0.9)

        # Create the layout managers
        main_layout = QVBoxLayout()

        # create the first row layout which includes eye-tracking and signal view
        sub_layout1 = QHBoxLayout()
        eye_tracking = QVBoxLayout()
        fNIRS = QVBoxLayout()
        EEG = QVBoxLayout()

        # Set the position and size of the widget
        self.setGeometry(x, y, width, height)

        # Set the position and size of the widget
        # self.setGeometry(200, 200, 400, 300)

        view_Label_fNIRS = QLabel("fNIRS")
        view_Label_EEG = QLabel("EEG")
        slider = QSlider(Qt.Horizontal, self)
        slider.setTickInterval(1)

        window = Window()
        signal_fNIRS = MainWindow()
        signal_EEG = WindowEEG()
        topo_fNIRS = TopoMainWindow()
        topo_EEG = TopoMainWindowEEG()

        slider.setMinimum(0)
        slider.setMaximum(50)
        slider.setGeometry(200, 1200, 100, 50)
        slider.setRange(0, 49)
        slider.valueChanged.connect(window.changedValue)
        slider.valueChanged.connect(signal_fNIRS.update_plot_data)
        slider.valueChanged.connect(topo_fNIRS.slider_moved)
        slider.valueChanged.connect(signal_EEG.update_plot_data)
        slider.valueChanged.connect(topo_EEG.slider_moved)
        slider.setTickPosition(QSlider.TicksBelow)

        # Add a border style to each label
        view_Label_fNIRS.setStyleSheet("border: 1px solid black;")
        view_Label_EEG.setStyleSheet("border: 1px solid black;")
        view_Label_fNIRS.setStyleSheet(
            "background-color: rgba(102, 102, 255, 100); padding: 2px;")
        view_Label_EEG.setStyleSheet(
            "background-color: rgba(102, 102, 255, 100); padding: 2px;")
        slider.setStyleSheet("border: 1px solid black;")

        # Set custom dimensions for each label
        view_Label_fNIRS.setFixedSize(int(width * 0.3), 50)
        view_Label_EEG.setFixedSize(int(width * 0.3), 50)
        slider.setFixedSize(1400, 50)

        # Set the stretch factor for the main layout to make box 1 take 2/3 of the vertical space
        main_layout.addLayout(sub_layout1)

        # Set the stretch factor for box 2 and box 3 to divide the remaining vertical space equally
        sub_layout1.addLayout(eye_tracking)
        sub_layout1.addLayout(fNIRS)
        sub_layout1.addLayout(EEG)

        # Create the second row layout
        sub_layout2 = QHBoxLayout()
        slider_box = QVBoxLayout()

        # Set the stretch factor for the second row layout to divide the vertical space equally
        main_layout.addLayout(sub_layout2)

        # Set the stretch factor for box 1 in the second row layout to make it 2/3 of the row's width
        sub_layout2.addLayout(slider_box)

        # Create the stacked widget for the views in Box 2
        stacked_widget_fNIRS = QStackedWidget()

        # Create the first view (View 1) and add it to the stacked widget
        stacked_widget_fNIRS.addWidget(signal_fNIRS)

        # Create the first view (View 1) and add it to the stacked widget
        stacked_widget_fNIRS.addWidget(topo_fNIRS)

        # Create the stacked widget for the views in Box 2
        stacked_widget_EEG = QStackedWidget()

        # Create the second view (View 2) and add it to the stacked widget
        stacked_widget_EEG.addWidget(signal_EEG)

        # Create the second view (View 2) and add it to the stacked widget
        stacked_widget_EEG.addWidget(topo_EEG)

        def switchButton_fNIRS():
            button1_property = button_fNIRS.property("value")
            # button2_property = button_EEG.property("value")
            # if button1_property == "fNIRS":
            # button_fNIRS.setProperty("value", "EEG")
            if button1_property == "signal":
                button_fNIRS.setProperty("value", "topological")
                stacked_widget_fNIRS.setCurrentIndex(1)
            elif button1_property == "topological":
                button_fNIRS.setProperty("value", "signal")
                stacked_widget_fNIRS.setCurrentIndex(0)
            # elif button1_property == "EEG":
            #     button_fNIRS.setProperty("value", "fNIRS")
            #     if button2_property == "signal":
            #         stacked_widget.setCurrentIndex(0)
            #     elif button2_property == "topological":
            #         stacked_widget.setCurrentIndex(2)

        def switchButton_EEG():
            # button1_property = button_fNIRS.property("value")
            button2_property = button_EEG.property("value")
            # if button2_property == "signal":
            # button_EEG.setProperty("value", "topological")
            if button2_property == "signal":
                button_EEG.setProperty("value", "topological")
                stacked_widget_EEG.setCurrentIndex(1)
            elif button2_property == "topological":
                button_EEG.setProperty("value", "signal")
                stacked_widget_EEG.setCurrentIndex(0)
            # elif button2_property == "topological":
            #     button_EEG.setProperty("value", "signal")
            #     if button1_property == "fNIRS":
            #         stacked_widget.setCurrentIndex(0)
            #     elif button1_property == "EEG":
            #         stacked_widget.setCurrentIndex(1)

        # Create a button
        button_fNIRS = QPushButton('fNIRS signal/Topo', self)
        # Set the property of button1 to indicate its value
        button_fNIRS.setProperty("value", "signal")
        color = QColor(102, 102, 255, 127)  # Purple color
        button_fNIRS.setStyleSheet("background-color: {}".format(color.name()))

        # Connect the button's clicked signal to a function
        button_fNIRS.clicked.connect(switchButton_fNIRS)

        # Create a button
        button_EEG = QPushButton('EEG signal/Topo', self)
        # Set the property of button2 to indicate its value
        button_EEG.setProperty("value", "signal")
        color = QColor(102, 102, 255, 215)  # Purple color
        button_EEG.setStyleSheet("background-color: {}".format(color.name()))

        # Connect the button's clicked signal to a function
        button_EEG.clicked.connect(switchButton_EEG)

        # Add the labels to the respective layouts
        eye_tracking.addWidget(window)
        fNIRS.addWidget(view_Label_fNIRS)
        fNIRS.addWidget(stacked_widget_fNIRS)
        fNIRS.addWidget(button_fNIRS)

        EEG.addWidget(view_Label_EEG)
        EEG.addWidget(stacked_widget_EEG)
        EEG.addWidget(button_EEG)

        slider_box.addWidget(slider)

        self.setLayout(main_layout)

        self.show()  # Show the widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show
    sys.exit(app.exec_())
