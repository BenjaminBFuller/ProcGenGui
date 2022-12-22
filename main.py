# Main.py
# Runs helper files to launch main window GUI
# In the main GUI contains the "About" window option and generation options
# Generating an image utilizes procgenmaps.py to procedural generate terrains with given user parameters

import sys
import os
from PySide2 import QtCore
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *

# Import UI config from python file generated by QT Designer
from ui_PROCGENGUI import Ui_PROCGEN, Ui_ABOUT

# Won't open on MAC OS X Big Sur and newer without this
os.environ["QT_MAC_WANTS_LAYER"] = "1"


class MainGUI(QMainWindow):
    def __init__(self):
        """Initializes main window"""
        QMainWindow.__init__(self)
        self.ui = Ui_PROCGEN()
        self.ui.setupUi(self)

        # Remove Frame & Title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.ui_frame.setGraphicsEffect(self.shadow)

        # Show window
        self.show()


class AboutGUI(QMainWindow):
    def __init__(self):
        """Initializes about window"""
        QMainWindow.__init__(self)
        self.uia = Ui_ABOUT()
        self.uia.setupUi(self)

        # Remove Frame & Title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.uia.ui_frame.setGraphicsEffect(self.shadow)


if __name__ == "__main__":
    # Deploy app, open the main window, wait for system exit while running
    app = QApplication()
    window = MainGUI()
    sys.exit(app.exec_())
