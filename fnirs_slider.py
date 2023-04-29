import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import sys
import pandas as pd

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        self.channel_list = [
            "S1-D1",
            "S1-D2",
            "S2-D1",
            "S2-D3",
            "S3-D1",
            "S3-D3",
            "S3-D4",
            "S4-D2",
            "S4-D4",
            "S4-D5",
            "S5-D3",
            "S5-D4",
            "S5-D6",
            "S6-D4",
            "S6-D6",
            "S6-D7",
            "S7-D5",
            "S7-D7",
            "S8-D6",
            "S8-D7",
        ]
        cwd = os.getcwd()
        data_path = os.path.join(cwd, "data/NIRS/NIRS_filtered.csv")

        data = pd.read_csv(
            data_path, sep='\t')
        
        self.data1 = data.iloc[:,1:21]
        self.data2 = data.iloc[:,21:41]

        # initialize plots
        super(MainWindow, self).__init__()

        # Create main layout
        self.mainLayout = QVBoxLayout()

        # Create and configure the plots layout
        self.graphWidgetLayout = pg.GraphicsLayoutWidget()
        self.graphWidgetLayout.resize(1000, 2500)

        # Create and configure the slider layout
        self.sliderLayout = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1000)
        self.slider.valueChanged.connect(self.update_plot_data)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.sliderLayout.addWidget(self.slider)

        # Add the plots and slider layouts to the main layout
        self.mainLayout.addWidget(self.graphWidgetLayout)
        self.mainLayout.addLayout(self.sliderLayout)

        # Set the main layout as the central widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

         # Enable antialiasing for prettier plots

        pg.setConfigOptions(antialias=True)

        self.graphWidgetLayout.setBackground("w")

        self.pen = pg.mkPen(color=(255, 0, 0), width=2)  # red for HbO
        self.pen1 = pg.mkPen(color=(0, 0, 255), width=2)  # blue for HbR

        self.ch = []
        self.ch1 = []

        label_style = {"color": (255, 0, 0), "font-size": "10pt"}

        # self.srate = 10  # 10.2Hz for NIRS data
        # self.timer = QtCore.QTimer()
        # # why? https://stackoverflow.com/questions/59094207/how-to-set-pyqt5-qtimer-to-update-in-specified-interval
        # self.timer.setInterval(round(1000 / self.srate))

        n_channels = len(self.channel_list)

        self.x = [0]
        self.y = [[0] for _ in range(n_channels)]  # HbO
        self.y1 = [[0] for _ in range(n_channels)]  # HbR

        self.dataLine = [[] for _ in range(n_channels)]
        self.dataLine1 = [[] for _ in range(n_channels)]

        for self.idx, self.channel in enumerate(self.channel_list):
            # create 20 subplots

            self.channel = self.graphWidgetLayout.addPlot(row=self.idx, col=0)
            # self.channel.showAxes('left', showValues=False)

            if self.idx < n_channels - 1:
                self.channel.hideAxis("bottom")

            self.channel.setLabel("left", self.channel_list[self.idx], **label_style)

            self.ch.append(self.channel)
            self.ch1.append(self.channel)

        self.plots()

    def plots(self):
        # draw

        for self.idx, (self.ch, self.ch1) in enumerate(zip(self.ch, self.ch1)):
            self.ch = self.ch.plot(x=self.x, y=self.y[self.idx], pen=self.pen)
            self.ch1 = self.ch1.plot(x=self.x, y=self.y1[self.idx], pen=self.pen1)

            self.dataLine[self.idx].append(self.ch)
            self.dataLine1[self.idx].append(self.ch1)

        # self.timer.timeout.connect(self.update_plot_data)
        # self.timer.start()

    def update_slider_value(self, value):
        self.slider_value = value
        
    def update_plot_data(self, value):
        self.slider_value = value

        window_size = 1000
        start = max(0, int(len(self.data1) * (self.slider_value / 1000) - window_size // 2))
        end = min(len(self.data1), start + window_size)

        self.x = list(range(start, end))

        for i in range(len(self.channel_list)):
            self.y[i] = self.data1.iloc[start:end, i].tolist()
            self.y1[i] = self.data2.iloc[start:end, i].tolist()

        for i in range(0, len(self.channel_list)):
            self.dataLine[i][0].setData(self.x, self.y[i])
            self.dataLine1[i][0].setData(self.x, self.y1[i])

    # def update_plot_data(self, value):
    #     self.slider_value = value
    #     # update data

    #     if len(self.x) >= 100:
    #         self.x = self.x[1:]  # Remove the first x element.

    #         for i in range(len(self.channel_list)):
    #             self.y[i] = self.y[i][1:]  # Remove the first
    #             self.y1[i] = self.y1[i][1:]  # Remove the first

    #     # Get the next chunk of samples from LSL.
    #     # They were accumulated while we were plotting the previous chunk
    #     # sample, time = self.inlet.pull_chunk()

    #     if len(self.data1) > 0:
    #         # Plot the most recent sample of this chunk. Discard the rest

    #         # Update the x value according to the number of samples we skipped
    #         self.x.append(self.x[-1] + len(self.data1.iloc[-1].values))

    #         # Append the last sample
    #         for i in range(len(self.channel_list)):
    #             # print(self.data1[-1][i], self.data2[-1][i])
    #             if self.slider_value == 0:
    #                 print('Im less than 0')
    #                 self.y[i].append(self.data1.iloc[-1][i])
    #                 self.y1[i].append(self.data2.iloc[-1][i])
    #             else:
    #                 print('Im greater than 0')
    #                 start = int(len(self.data1) * (self.slider_value / 1000))
    #                 end = int(len(self.data1) * ((self.slider_value + 1) / 1000))
    #                 self.y[i].append(self.data1.iloc[start:end, i].mean())
    #                 self.y1[i].append(self.data2.iloc[start:end, i].mean())
    #                 print(self.data1.iloc[start:end, i], self.data2.iloc[start:end, i])

    #         for i in range(0, len(self.channel_list)):
    #             self.dataLine[i][0].setData(self.x, self.y[i])
    #             self.dataLine1[i][0].setData(self.x, self.y1[i])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
