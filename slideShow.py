import sys
import argparse
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

# def slidshow():
    # s = SlideShow()
    # s.setFilenames(['/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064391.png', '/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064390.png'])
    # s.show()

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #     description="ToMCAT post experiment complete replay"
    # )
    # parser.add_argument(
    #     "--ss",
    #     required=True,
    #     help="Path to screenshot folder",
    # )

    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames(['/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064391.png', '/Users/calebjonesshibu/Desktop/tom/pilot/exp_2022_11_08_11/tiger/screenshots/output064390.png'])
    s.show()
    app.exec_()