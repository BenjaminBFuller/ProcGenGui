# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PROCGENGUICYdHbF.ui'
## Benjamin Fuller
## Created by: Qt User Interface Compiler version 5.15.5
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from functools import partial
import procgenmaps as pgm
from ui_AboutWindow import Ui_ABOUT


class Ui_PROCGEN(object):
    def __init__(self):
        super().__init__()
        self.biome = "Islands"
        self.scale = "50"
        self.shape = "400x400"
        self.octaves = "1"

    def setupUi(self, PROCGEN):
        if not PROCGEN.objectName():
            PROCGEN.setObjectName("PROCGEN")
        PROCGEN.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PROCGEN.sizePolicy().hasHeightForWidth())
        PROCGEN.setSizePolicy(sizePolicy)
        PROCGEN.setMinimumSize(QSize(400, 400))
        PROCGEN.setMaximumSize(QSize(400, 400))
        font = QFont()
        font.setFamily("Charter")
        PROCGEN.setFont(font)
        PROCGEN.setCursor(QCursor(Qt.ArrowCursor))
        PROCGEN.setMouseTracking(True)
        PROCGEN.setTabletTracking(True)
        PROCGEN.setAutoFillBackground(True)
        PROCGEN.setStyleSheet("")
        self.ui_frame = QFrame(PROCGEN)
        self.ui_frame.setObjectName("ui_frame")
        self.ui_frame.setGeometry(QRect(10, 10, 381, 381))
        sizePolicy.setHeightForWidth(self.ui_frame.sizePolicy().hasHeightForWidth())
        self.ui_frame.setSizePolicy(sizePolicy)
        self.ui_frame.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(".AppleSystemUIFont")
        self.ui_frame.setFont(font1)
        self.ui_frame.setStyleSheet(
            "QFrame {\n"
            "	background-color: rgb(0, 123, 215);\n"
            "	color: rgb(255, 255, 255);\n"
            "	border-radius: 10px\n"
            "}"
        )
        self.ui_frame.setFrameShape(QFrame.StyledPanel)
        self.ui_frame.setFrameShadow(QFrame.Raised)
        self.shape_frame = QFrame(self.ui_frame)
        self.shape_frame.setObjectName("shape_frame")
        self.shape_frame.setGeometry(QRect(80, 130, 91, 41))
        self.shape_frame.setStyleSheet(
            "background-color: rgb(255, 147, 0);\n" "border-radius: 10px;"
        )
        self.shape_frame.setFrameShape(QFrame.StyledPanel)
        self.shape_frame.setFrameShadow(QFrame.Raised)
        self.shape_label = QLabel(self.shape_frame)
        self.shape_label.setObjectName("shape_label")
        self.shape_label.setGeometry(QRect(0, 10, 91, 21))
        self.shape_label.setStyleSheet("")
        self.shape_label.setAlignment(Qt.AlignCenter)
        self.scale_frame = QFrame(self.ui_frame)
        self.scale_frame.setObjectName("scale_frame")
        self.scale_frame.setGeometry(QRect(80, 190, 91, 41))
        self.scale_frame.setStyleSheet(
            "background-color: rgb(255, 147, 0);\n" "border-radius: 10px;"
        )
        self.scale_frame.setFrameShape(QFrame.StyledPanel)
        self.scale_frame.setFrameShadow(QFrame.Raised)
        self.scale_label = QLabel(self.scale_frame)
        self.scale_label.setObjectName("scale_label")
        self.scale_label.setGeometry(QRect(0, 10, 91, 21))
        self.scale_label.setStyleSheet("")
        self.scale_label.setAlignment(Qt.AlignCenter)
        self.octaves_frame = QFrame(self.ui_frame)
        self.octaves_frame.setObjectName("octaves_frame")
        self.octaves_frame.setGeometry(QRect(80, 250, 91, 41))
        self.octaves_frame.setStyleSheet(
            "background-color: rgb(255, 147, 0);\n" "border-radius: 10px;"
        )
        self.octaves_frame.setFrameShape(QFrame.StyledPanel)
        self.octaves_frame.setFrameShadow(QFrame.Raised)
        self.octaves_label = QLabel(self.octaves_frame)
        self.octaves_label.setObjectName("octaves_label")
        self.octaves_label.setGeometry(QRect(-1, 10, 91, 21))
        self.octaves_label.setStyleSheet("")
        self.octaves_label.setAlignment(Qt.AlignCenter)
        self.biomes_frame = QFrame(self.ui_frame)
        self.biomes_frame.setObjectName("biomes_frame")
        self.biomes_frame.setGeometry(QRect(80, 70, 91, 41))
        self.biomes_frame.setStyleSheet(
            "background-color: rgb(255, 147, 0);\n" "border-radius: 10px;"
        )
        self.biomes_frame.setFrameShape(QFrame.StyledPanel)
        self.biomes_frame.setFrameShadow(QFrame.Raised)
        self.biomes_label = QLabel(self.biomes_frame)
        self.biomes_label.setObjectName("biomes_label")
        self.biomes_label.setGeometry(QRect(-1, 9, 91, 21))
        self.biomes_label.setFont(font1)
        self.biomes_label.setStyleSheet("")
        self.biomes_label.setAlignment(Qt.AlignCenter)
        self.generate_button = QPushButton(self.ui_frame)
        # Generate map with selected combobox values upon click
        self.generate_button.clicked.connect(
            partial(
                self.on_generation_click,
                self.biome,
                self.scale,
                self.shape,
                self.octaves,
            )
        )
        self.generate_button.setObjectName("generate_button")
        self.generate_button.setGeometry(QRect(190, 310, 113, 32))
        self.reset_button = QPushButton(self.ui_frame)
        # Exit upon clicking reset button
        self.reset_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setGeometry(QRect(70, 310, 113, 32))
        self.comboBox_biomes = QComboBox(self.ui_frame)
        self.comboBox_biomes.activated[str].connect(self.on_biomes_click)
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.addItem("")
        self.comboBox_biomes.setObjectName("comboBox_biomes")
        self.comboBox_biomes.setGeometry(QRect(190, 70, 111, 41))
        self.comboBox_shape = QComboBox(self.ui_frame)
        self.comboBox_shape.activated[str].connect(self.on_shape_click)
        self.comboBox_shape.addItem("")
        self.comboBox_shape.addItem("")
        self.comboBox_shape.addItem("")
        self.comboBox_shape.setObjectName("comboBox_shape")
        self.comboBox_shape.setGeometry(QRect(190, 130, 111, 41))
        self.comboBox_scale = QComboBox(self.ui_frame)
        self.comboBox_scale.activated[str].connect(self.on_scale_click)
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.setObjectName("comboBox_scale")
        self.comboBox_scale.setGeometry(QRect(190, 190, 111, 41))
        self.comboBox_4 = QComboBox(self.ui_frame)
        self.comboBox_4.activated[str].connect(self.on_octaves_click)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setGeometry(QRect(190, 250, 111, 41))
        self.title_label = QLabel(self.ui_frame)
        self.title_label.setObjectName("title_label")
        self.title_label.setGeometry(QRect(10, 9, 361, 51))
        font2 = QFont()
        font2.setFamily(".AppleSystemUIFont")
        font2.setPointSize(39)
        self.title_label.setFont(font2)
        self.title_label.setStyleSheet("")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.about_button = QPushButton(self.ui_frame)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setGeometry(QRect(340, 10, 31, 31))
        self.about_button.clicked.connect(self.on_about_click)

        self.retranslateUi(PROCGEN)

        QMetaObject.connectSlotsByName(PROCGEN)

    # setupUi
    def retranslateUi(self, PROCGEN):
        PROCGEN.setWindowTitle(QCoreApplication.translate("PROCGEN", "PROCGEN", None))
        self.shape_label.setText(QCoreApplication.translate("PROCGEN", "SHAPE", None))
        self.scale_label.setText(QCoreApplication.translate("PROCGEN", "SCALE", None))
        self.octaves_label.setText(
            QCoreApplication.translate("PROCGEN", "OCTAVES", None)
        )
        self.biomes_label.setText(QCoreApplication.translate("PROCGEN", "BIOME", None))
        self.generate_button.setText(
            QCoreApplication.translate("PROCGEN", "Generate", None)
        )
        self.reset_button.setText(QCoreApplication.translate("PROCGEN", "Exit", None))
        self.comboBox_biomes.setItemText(
            0, QCoreApplication.translate("PROCGEN", "Islands", None)
        )
        self.comboBox_biomes.setItemText(
            1, QCoreApplication.translate("PROCGEN", "Forest", None)
        )
        self.comboBox_biomes.setItemText(
            2, QCoreApplication.translate("PROCGEN", "Desert Oasis", None)
        )
        self.comboBox_biomes.setItemText(
            3, QCoreApplication.translate("PROCGEN", "Cherry Blossom", None)
        )
        self.comboBox_biomes.setItemText(
            4, QCoreApplication.translate("PROCGEN", "Caves", None)
        )
        self.comboBox_biomes.setItemText(
            5, QCoreApplication.translate("PROCGEN", "Terraces", None)
        )
        self.comboBox_biomes.setItemText(
            6, QCoreApplication.translate("PROCGEN", "Clouds", None)
        )

        self.comboBox_shape.setItemText(
            0, QCoreApplication.translate("PROCGEN", "400x400", None)
        )
        self.comboBox_shape.setItemText(
            1, QCoreApplication.translate("PROCGEN", "600x600", None)
        )
        self.comboBox_shape.setItemText(
            2, QCoreApplication.translate("PROCGEN", "800x800", None)
        )

        self.comboBox_scale.setItemText(
            0, QCoreApplication.translate("PROCGEN", "50", None)
        )
        self.comboBox_scale.setItemText(
            1, QCoreApplication.translate("PROCGEN", "100", None)
        )
        self.comboBox_scale.setItemText(
            2, QCoreApplication.translate("PROCGEN", "200", None)
        )
        self.comboBox_scale.setItemText(
            3, QCoreApplication.translate("PROCGEN", "300", None)
        )
        self.comboBox_scale.setItemText(
            4, QCoreApplication.translate("PROCGEN", "400", None)
        )
        self.comboBox_scale.setItemText(
            5, QCoreApplication.translate("PROCGEN", "500", None)
        )
        self.comboBox_scale.setItemText(
            6, QCoreApplication.translate("PROCGEN", "600", None)
        )
        self.comboBox_scale.setItemText(
            7, QCoreApplication.translate("PROCGEN", "700", None)
        )
        self.comboBox_scale.setItemText(
            8, QCoreApplication.translate("PROCGEN", "800", None)
        )
        self.comboBox_scale.setItemText(
            9, QCoreApplication.translate("PROCGEN", "900", None)
        )
        self.comboBox_scale.setItemText(
            10, QCoreApplication.translate("PROCGEN", "1000", None)
        )

        self.comboBox_4.setItemText(0, QCoreApplication.translate("PROCGEN", "1", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("PROCGEN", "2", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("PROCGEN", "3", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("PROCGEN", "4", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("PROCGEN", "5", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("PROCGEN", "6", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("PROCGEN", "7", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("PROCGEN", "8", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("PROCGEN", "9", None))
        self.comboBox_4.setItemText(
            9, QCoreApplication.translate("PROCGEN", "10", None)
        )
        self.title_label.setText(
            QCoreApplication.translate(
                "PROCGEN",
                '<html><head/><body><p><span style=" font-weight:600;">M A P G E N</span></p></body></html>',
                None,
            )
        )
        self.about_button.setText(QCoreApplication.translate("PROCGEN", u"?", None))

    # retranslateUi

    def on_biomes_click(self):
        self.biome = self.comboBox_biomes.currentText()

    def on_octaves_click(self):
        self.octaves = self.comboBox_4.currentText()

    def on_shape_click(self):
        self.shape = self.comboBox_shape.currentText()

    def on_scale_click(self):
        self.scale = self.comboBox_scale.currentText()

    def on_generation_click(self, biome, scale, shape, octaves):
        # print(self.biome, self.scale, self.shape, self.octaves)
        pgm.generate_map(self.biome, self.scale, self.shape, self.octaves)

    def on_about_click(self):
        self.w = AboutGUI()
        self.w.show()


class AboutGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ABOUT()
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