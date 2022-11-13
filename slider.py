#!/usr/bin/python
from pyqt_slideshow import SlideShow
from PyQt6.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    #     self.disp_img()

    # def disp_img(self):
    #     label = QLabel(self)
    #     pixmap = QPixmap('/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064391.png')
    #     label.setPixmap(pixmap)
    #     self.setCentralWidget(label)
    #     self.resize(pixmap.width(), pixmap.height())


    def initUI(self):
            
        hbox = QHBoxLayout()
        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setRange(0, 100)
        sld.setPageStep(1)

        sld.valueChanged.connect(self.updateLabel)

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter |
                                Qt.AlignmentFlag.AlignVCenter)
        self.label.setMinimumWidth(80)

        hbox.addWidget(sld)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(100, 100, 100, 100) #position of app and dimension of the app
        self.setWindowTitle('QSlider')
        self.show()

    def updateLabel(self, value):
        self.label.setText(str(value)) #value gets updates as soon you move the slider
        print(str(value))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
