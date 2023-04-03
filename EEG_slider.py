from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import sys
import pandas as pd

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        self.channel_list = [
            "AFF1h",
            "AFF5h",
            "F7",
            "FC5",
            "FC1",
            "C3",
            "T7",
            "TP9",
            "CP5",
            "CP1",
            "Pz",
            "P3",
            "P7",
            "PO9",
            "O1",
            "Oz",
            "O2",
            "PO10",
            "P8",
            "P4",
            "TP10",
            "CP6",
            "CP2",
            "Cz",
            "C4",
            "T8",
            "FC6",
            "FC2",
            "FCz",
            "F8",
            "AFF6h",
            "AFF2h",
            "AUX_GSR",
            "AUX_EKG",
        ]

        self.channels_used = [
            "AFF1h",
            "F7",
            "FC5",
            "C3",
            "T7",
            "TP9",
            "Pz",
            "P3",
            "P7",
            "O1",
            "O2",
            "P8",
            "P4",
            "TP10",
            "Cz",
            "C4",
            "T8",
            "FC6",
            "FCz",
            "F8",
            "AFF2h",
            "AUX_GSR",
            "AUX_EKG",
        ]

        data = pd.read_csv("/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/eeg_fnirs_pupil/eeg_fnirs_pupil/EEG.csv",sep = '\t')
        # Get the index of channel that are being used.
        self.channel_indices = [data.columns.get_loc(channel) for channel in self.channels_used]

        self.data1 = data.iloc[:, self.channel_indices]
        # self.data2 = data.iloc[:,21:41]

        print(self.data1.shape)

        # initialize plots
        super(MainWindow, self).__init__()

        self.graphWidgetLayout = pg.GraphicsLayoutWidget()
        self.graphWidgetLayout.resize(1000, 2500)
        self.setCentralWidget(self.graphWidgetLayout)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setTickInterval(1)

        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        self.slider.setGeometry(50, 1200, 1000, 20)
        self.slider.valueChanged.connect(self.update_plot_data)
        self.slider.setTickPosition(QSlider.TicksBelow)
        # Enable antialiasing for prettier plots

        pg.setConfigOptions(antialias=True)

        self.graphWidgetLayout.setBackground("w")

        self.pen = pg.mkPen(color=(0, 0, 0), width=2)  # red for HbO
        # self.pen1 = pg.mkPen(color=(0, 0, 255), width=2)  # blue for HbR

        self.ch = []
        # self.ch1 = []

        label_style = {"color": (255, 0, 0), "font-size": "10pt"}

        # self.srate = 10  # 10.2Hz for NIRS data
        # self.timer = QtCore.QTimer()
        # # why? https://stackoverflow.com/questions/59094207/how-to-set-pyqt5-qtimer-to-update-in-specified-interval
        # self.timer.setInterval(round(1000 / self.srate))

        n_channels = len(self.channels_used)

        self.x = [0]
        self.y = [[0] for _ in range(n_channels)]  # HbO
        # self.y1 = [[0] for _ in range(n_channels)]  # HbR

        self.dataLine = [[] for _ in range(n_channels)]
        # self.dataLine1 = [[] for _ in range(n_channels)]

        for self.idx, self.channel in enumerate(self.channels_used):
            # create 20 subplots

            self.channel = self.graphWidgetLayout.addPlot(row=self.idx, col=0)
            # self.channel.showAxes('left', showValues=False)

            if self.idx < n_channels - 1:
                self.channel.hideAxis("bottom")

            self.channel.setLabel("left", self.channels_used[self.idx], **label_style)

            self.ch.append(self.channel)
            # self.ch1.append(self.channel)

        self.plots()

    def plots(self):
        # draw

        for self.idx, self.ch in enumerate(self.ch):
            self.ch = self.ch.plot(x=self.x, y=self.y[self.idx], pen=self.pen)
            # self.ch1 = self.ch1.plot(x=self.x, y=self.y1[self.idx], pen=self.pen1)

            self.dataLine[self.idx].append(self.ch)
            # self.dataLine1[self.idx].append(self.ch1)

        # self.timer.timeout.connect(self.update_plot_data)
        # self.timer.start()

    def update_slider_value(self, value):
            self.slider_value = value

        

    def update_plot_data(self, value):
        self.slider_value = value

        for i in range(len(self.channels_used)):
            start = int(len(self.data1) * (self.slider_value / 1000))
            end = int(len(self.data1) * ((self.slider_value + 1) / 1000))
            self.y[i] = list(self.data1.iloc[start:end, i].values)
            self.dataLine[i][0].setData(self.x[:len(self.y[i])], self.y[i])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())