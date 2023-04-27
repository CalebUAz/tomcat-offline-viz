import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 900
        self.initUI()

    def initUI(self):
        self.setGeometry(self.width, self.width, self.height, self.height)  # Set the position and size of the widget

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.tab_widget2 = QTabWidget()
        vbox.addWidget(self.tab_widget)
        vbox.addWidget(self.tab_widget2)

        # self.button = QPushButton('Click me', self)  # Create a button

        # vbox.addWidget(self.button)
        # self.button.clicked.connect(self.on_button_clicked)  # Connect the button's clicked signal to a function

        # self.label = QLabel(self)  # Create a label
        # self.label.setText('Button not clicked yet')  # Set the initial text for the label
        # self.label.move(10, 50)  # Move the label to a specific position

        self.show()  # Show the widget

    def on_button_clicked(self):
        self.label.setText('Button clicked')  # Update the label's text when the button is clicked


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
