import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("Data Plotting")
        self.data = data
        self.channels = len(self.data.columns)

        # Create the plot widget
        self.plot_widget = QWidget(self)
        self.plot_layout = QVBoxLayout(self.plot_widget)
        self.plot_canvas = FigureCanvas(Figure(figsize=(12, 12)))
        self.plot_layout.addWidget(self.plot_canvas)

        # Create the slider widget
        self.slider = QSlider(self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.data)-100)
        self.slider.setOrientation(1)
        self.slider.setTickInterval(100)
        self.slider.setTickPosition(QSlider.TicksBelow)

        # Create the label widget
        self.label = QLabel(self)
        self.label.setText("Current Index: 0")

        # Add the slider and label widgets to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.slider)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.plot_widget)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect the slider signal to the update plot function
        self.slider.valueChanged.connect(self.update_plot)

        # Update the plot for the initial slider value
        self.update_plot(0)

    def update_plot(self, value):
        # Get the current index from the slider value
        idx = value

        # Clear the previous plot
        self.plot_canvas.figure.clf()

        # Create 20 subplots
        fig, axs = plt.subplots(nrows=20, sharex=True, figsize=(10, 20))

        # Plot the data for each channel in a separate subplot
        for i in range(self.channels):
            channel_data = self.data.iloc[idx:idx+100, i]
            axs[i].plot(channel_data)
            axs[i].set_title(f"Channel {i+1}")
            axs[i].set_ylabel("Amplitude")

        # Set the x-axis label for the last subplot
        axs[-1].set_xlabel("Samples")

        # Set the title for the entire plot
        fig.suptitle("Data Plot")

        # Draw the plot
        self.plot_canvas.draw()

        # Update the label text
        self.label.setText(f"Current Index: {idx}")


if __name__ == "__main__":
    # Load data from CSV file
    data = pd.read_csv("/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/eeg_fnirs_pupil/eeg_fnirs_pupil/NIRS_filtered.csv",sep = '\t')
    data = data.iloc[:,1:20]

    # Create the Qt application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow(data)

    # Show the main window and start the event loop
    main_window.show()
    sys.exit(app.exec_())

# import sys
# import pandas as pd
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QWidget
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure

# class MainWindow(QMainWindow):
#     def __init__(self, data):
#         super().__init__()

#         self.setWindowTitle("Data Plotting")
#         self.data = data
#         self.channels = len(self.data.columns)

#         # Create the plot widget
#         self.plot_widget = QWidget(self)
#         self.plot_layout = QVBoxLayout(self.plot_widget)
#         self.plot_canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         self.plot_layout.addWidget(self.plot_canvas)

#         # Create the slider widget
#         self.slider = QSlider(self)
#         self.slider.setMinimum(0)
#         self.slider.setMaximum(len(self.data)-100)
#         self.slider.setOrientation(1)
#         self.slider.setTickInterval(100)
#         self.slider.setTickPosition(QSlider.TicksBelow)

#         # Create the label widget
#         self.label = QLabel(self)
#         self.label.setText("Current Index: 0")

#         # Add the slider and label widgets to the main layout
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(self.slider)
#         main_layout.addWidget(self.label)
#         main_layout.addWidget(self.plot_widget)
#         central_widget = QWidget()
#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#         # Connect the slider signal to the update plot function
#         self.slider.valueChanged.connect(self.update_plot)

#         # Update the plot for the initial slider value
#         self.update_plot(0)

#     def update_plot(self, value):
#         # Get the current index from the slider value
#         idx = value

#         # Clear the previous plot
#         self.plot_canvas.figure.clf()

#         # Create a new plot
#         ax = self.plot_canvas.figure.add_subplot(111)

#         # Plot the data for each channel
#         for i in range(self.channels):
#             channel_data = self.data.iloc[idx:idx+100, i]
#             ax.plot(channel_data)

#         # Set the title and axis labels
#         ax.set_title("Data Plot")
#         ax.set_xlabel("Samples")
#         ax.set_ylabel("Amplitude")

#         # Draw the plot
#         self.plot_canvas.draw()

#         # Update the label text
#         self.label.setText(f"Current Index: {idx}")

# if __name__ == "__main__":
#     # Load data from CSV file
#     data = pd.read_csv("/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/eeg_fnirs_pupil/eeg_fnirs_pupil/NIRS_filtered.csv",sep = '\t')
#     data = data.iloc[:,1:20]

#     # Create the Qt application and main window
#     app = QApplication(sys.argv)
#     main_window = MainWindow(data)

#     # Show the main window and start the event loop
#     main_window.show()
#     sys.exit(app.exec_())



# data = pd.read_csv("/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/eeg_fnirs_pupil/eeg_fnirs_pupil/NIRS_filtered.csv",sep = '\t')
# data = data.iloc[:,1:20]

# self.data = pd.read_csv("/Users/calebjonesshibu/Desktop/tom/exp_2023_02_03_10/tiger/eeg_fnirs_pupil/eeg_fnirs_pupil/NIRS_filtered.csv",sep = '\t')
# self.data = self.data.iloc[:,1:20].to_numpy()