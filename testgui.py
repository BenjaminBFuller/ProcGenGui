from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
import sys


class FramelessWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.label = QLabel("Hello world", self)
        self.offset = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FramelessWidget()
    win.setGeometry(300, 300, 300, 300)
    win.show()
    sys.exit(app.exec_())
