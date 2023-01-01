# Form generated from reading UI file 'PROCGENGUICYdHbF.ui'
# Benjamin Fuller
# Created by: Qt User Interface Compiler version 5.15.5
# WARNING! All changes made in this file will be lost when recompiling UI file!


# imports
from PySide2 import QtCore
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from functools import partial
import procgenmaps as pgm


class Ui_PROCGEN(object):
    # initialize super object and base (lowest/1st) settings for generation on UI window comboboxes
    def __init__(self):
        super().__init__()
        self.biome = "Islands"
        self.scale = "50"
        self.shape = "400x400"
        self.octaves = "1"

    # QT Designer generated code for UI structure
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

        self.retranslateProcgenUi(PROCGEN)

        QMetaObject.connectSlotsByName(PROCGEN)

    # add labels throughout (Titles, combo box elements,...) after UI generation
    def retranslateProcgenUi(self, PROCGEN):
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
        self.comboBox_biomes.setItemText(
            7, QCoreApplication.translate("PROCGEN", "Rainbow", None)
        )
        self.comboBox_biomes.setItemText(
            8, QCoreApplication.translate("PROCGEN", "Graylands", None)
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
                '<html><head/><body><p><span style=" font-weight:600;">P R O C G E N</span></p></body></html>',
                None,
            )
        )
        self.about_button.setText(QCoreApplication.translate("PROCGEN", u"?", None))

    # Click functions: update variables on click with given user parameters
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


# About window generation and setup with QT Designer
class Ui_ABOUT(object):
    def setupUi(self, ABOUT):
        if not ABOUT.objectName():
            ABOUT.setObjectName(u"ABOUT")
        ABOUT.resize(610, 670)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ABOUT.sizePolicy().hasHeightForWidth())
        ABOUT.setSizePolicy(sizePolicy)
        ABOUT.setMinimumSize(QSize(400, 400))
        ABOUT.setMaximumSize(QSize(610, 670))
        font = QFont()
        font.setFamily(u"Charter")
        ABOUT.setFont(font)
        ABOUT.setCursor(QCursor(Qt.UpArrowCursor))
        ABOUT.setMouseTracking(True)
        ABOUT.setTabletTracking(True)
        ABOUT.setAutoFillBackground(True)
        ABOUT.setStyleSheet(u"")
        self.ui_frame = QFrame(ABOUT)
        self.ui_frame.setObjectName(u"ui_frame")
        self.ui_frame.setGeometry(QRect(10, 10, 591, 651))
        sizePolicy.setHeightForWidth(self.ui_frame.sizePolicy().hasHeightForWidth())
        self.ui_frame.setSizePolicy(sizePolicy)
        self.ui_frame.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u".AppleSystemUIFont")
        self.ui_frame.setFont(font1)
        self.ui_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.ui_frame.setStyleSheet(u"QFrame {\n"
                                    "	background-color: rgb(120, 200, 255);\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	border-radius: 10px\n"
                                    "}")
        self.ui_frame.setFrameShape(QFrame.StyledPanel)
        self.ui_frame.setFrameShadow(QFrame.Raised)
        self.shape_frame = QFrame(self.ui_frame)
        self.shape_frame.setObjectName(u"shape_frame")
        self.shape_frame.setGeometry(QRect(300, 70, 271, 251))
        self.shape_frame.setStyleSheet(u"background-color: rgb(255, 217, 140);\n"
                                       "border-radius: 10px;\n"
                                       "color: rgb(0, 0, 0);")
        self.shape_frame.setFrameShape(QFrame.StyledPanel)
        self.shape_frame.setFrameShadow(QFrame.Raised)
        self.shape_label = QLabel(self.shape_frame)
        self.shape_label.setObjectName(u"shape_label")
        self.shape_label.setGeometry(QRect(0, 10, 271, 21))
        self.shape_label.setStyleSheet(u"")
        self.shape_label.setAlignment(Qt.AlignCenter)
        self.shape_label_2 = QLabel(self.shape_frame)
        self.shape_label_2.setObjectName(u"shape_label_2")
        self.shape_label_2.setGeometry(QRect(0, 40, 271, 21))
        self.shape_label_2.setStyleSheet(u"")
        self.shape_label_2.setAlignment(Qt.AlignCenter)
        self.shape_label_3 = QLabel(self.shape_frame)
        self.shape_label_3.setObjectName(u"shape_label_3")
        self.shape_label_3.setGeometry(QRect(0, 60, 271, 21))
        self.shape_label_3.setStyleSheet(u"")
        self.shape_label_3.setAlignment(Qt.AlignCenter)
        self.shape_label_4 = QLabel(self.shape_frame)
        self.shape_label_4.setObjectName(u"shape_label_4")
        self.shape_label_4.setGeometry(QRect(0, 80, 271, 21))
        self.shape_label_4.setStyleSheet(u"")
        self.shape_label_4.setAlignment(Qt.AlignCenter)
        self.shape_label_5 = QLabel(self.shape_frame)
        self.shape_label_5.setObjectName(u"shape_label_5")
        self.shape_label_5.setGeometry(QRect(10, 200, 41, 41))
        self.shape_label_5.setStyleSheet(u"")
        self.shape_label_5.setPixmap(QPixmap(u"imgs/terrace_chunk.png"))
        self.shape_label_5.setAlignment(Qt.AlignCenter)
        self.shape_label_6 = QLabel(self.shape_frame)
        self.shape_label_6.setObjectName(u"shape_label_6")
        self.shape_label_6.setGeometry(QRect(60, 170, 71, 71))
        self.shape_label_6.setStyleSheet(u"")
        self.shape_label_6.setPixmap(QPixmap(u"imgs/terrace_chunk.png"))
        self.shape_label_6.setAlignment(Qt.AlignCenter)
        self.shape_label_7 = QLabel(self.shape_frame)
        self.shape_label_7.setObjectName(u"shape_label_7")
        self.shape_label_7.setGeometry(QRect(140, 120, 121, 121))
        self.shape_label_7.setStyleSheet(u"")
        self.shape_label_7.setPixmap(QPixmap(u"imgs/terrace_chunk.png"))
        self.shape_label_7.setAlignment(Qt.AlignCenter)
        self.scale_frame = QFrame(self.ui_frame)
        self.scale_frame.setObjectName(u"scale_frame")
        self.scale_frame.setGeometry(QRect(20, 330, 271, 251))
        self.scale_frame.setStyleSheet(u"background-color: rgb(255, 217, 140);\n"
                                       "border-radius: 10px;\n"
                                       "color: rgb(0, 0, 0);")
        self.scale_frame.setFrameShape(QFrame.StyledPanel)
        self.scale_frame.setFrameShadow(QFrame.Raised)
        self.scale_label = QLabel(self.scale_frame)
        self.scale_label.setObjectName(u"scale_label")
        self.scale_label.setGeometry(QRect(0, 10, 271, 21))
        self.scale_label.setStyleSheet(u"")
        self.scale_label.setAlignment(Qt.AlignCenter)
        self.scale_label_2 = QLabel(self.scale_frame)
        self.scale_label_2.setObjectName(u"scale_label_2")
        self.scale_label_2.setGeometry(QRect(0, 40, 271, 21))
        self.scale_label_2.setStyleSheet(u"")
        self.scale_label_2.setAlignment(Qt.AlignCenter)
        self.scale_label_3 = QLabel(self.scale_frame)
        self.scale_label_3.setObjectName(u"scale_label_3")
        self.scale_label_3.setGeometry(QRect(0, 60, 271, 21))
        self.scale_label_3.setStyleSheet(u"")
        self.scale_label_3.setAlignment(Qt.AlignCenter)
        self.scale_label_4 = QLabel(self.scale_frame)
        self.scale_label_4.setObjectName(u"scale_label_4")
        self.scale_label_4.setGeometry(QRect(0, 80, 271, 21))
        self.scale_label_4.setStyleSheet(u"")
        self.scale_label_4.setAlignment(Qt.AlignCenter)
        self.scale_label_5 = QLabel(self.scale_frame)
        self.scale_label_5.setObjectName(u"scale_label_5")
        self.scale_label_5.setGeometry(QRect(10, 120, 121, 121))
        self.scale_label_5.setStyleSheet(u"")
        self.scale_label_5.setPixmap(QPixmap(u"imgs/clouds_zoom_in.png"))
        self.scale_label_5.setScaledContents(True)
        self.scale_label_5.setAlignment(Qt.AlignCenter)
        self.scale_label_6 = QLabel(self.scale_frame)
        self.scale_label_6.setObjectName(u"scale_label_6")
        self.scale_label_6.setGeometry(QRect(140, 120, 121, 121))
        self.scale_label_6.setStyleSheet(u"")
        self.scale_label_6.setPixmap(QPixmap(u"imgs/clouds_zoom_out.png"))
        self.scale_label_6.setScaledContents(True)
        self.scale_label_6.setAlignment(Qt.AlignCenter)
        self.octaves_frame = QFrame(self.ui_frame)
        self.octaves_frame.setObjectName(u"octaves_frame")
        self.octaves_frame.setGeometry(QRect(300, 330, 271, 251))
        self.octaves_frame.setStyleSheet(u"background-color: rgb(255, 217, 140);\n"
                                         "border-radius: 10px;\n"
                                         "color: rgb(0, 0, 0);")
        self.octaves_frame.setFrameShape(QFrame.StyledPanel)
        self.octaves_frame.setFrameShadow(QFrame.Raised)
        self.octaves_label = QLabel(self.octaves_frame)
        self.octaves_label.setObjectName(u"octaves_label")
        self.octaves_label.setGeometry(QRect(-1, 10, 271, 21))
        self.octaves_label.setStyleSheet(u"")
        self.octaves_label.setAlignment(Qt.AlignCenter)
        self.octaves_label_2 = QLabel(self.octaves_frame)
        self.octaves_label_2.setObjectName(u"octaves_label_2")
        self.octaves_label_2.setGeometry(QRect(0, 40, 271, 21))
        self.octaves_label_2.setStyleSheet(u"")
        self.octaves_label_2.setAlignment(Qt.AlignCenter)
        self.octaves_label_3 = QLabel(self.octaves_frame)
        self.octaves_label_3.setObjectName(u"octaves_label_3")
        self.octaves_label_3.setGeometry(QRect(0, 60, 271, 21))
        self.octaves_label_3.setStyleSheet(u"")
        self.octaves_label_3.setAlignment(Qt.AlignCenter)
        self.octaves_label_4 = QLabel(self.octaves_frame)
        self.octaves_label_4.setObjectName(u"octaves_label_4")
        self.octaves_label_4.setGeometry(QRect(0, 80, 271, 21))
        self.octaves_label_4.setStyleSheet(u"")
        self.octaves_label_4.setAlignment(Qt.AlignCenter)
        self.octaves_label_5 = QLabel(self.octaves_frame)
        self.octaves_label_5.setObjectName(u"octaves_label_5")
        self.octaves_label_5.setGeometry(QRect(10, 120, 121, 121))
        self.octaves_label_5.setStyleSheet(u"")
        self.octaves_label_5.setPixmap(QPixmap(u"imgs/rainbow_low.png"))
        self.octaves_label_5.setScaledContents(True)
        self.octaves_label_5.setAlignment(Qt.AlignCenter)
        self.octaves_label_6 = QLabel(self.octaves_frame)
        self.octaves_label_6.setObjectName(u"octaves_label_6")
        self.octaves_label_6.setGeometry(QRect(140, 120, 121, 121))
        self.octaves_label_6.setStyleSheet(u"")
        self.octaves_label_6.setPixmap(QPixmap(u"imgs/rainbow_high.png"))
        self.octaves_label_6.setScaledContents(True)
        self.octaves_label_6.setAlignment(Qt.AlignCenter)
        self.biomes_frame = QFrame(self.ui_frame)
        self.biomes_frame.setObjectName(u"biomes_frame")
        self.biomes_frame.setGeometry(QRect(20, 70, 271, 251))
        self.biomes_frame.setStyleSheet(u"background-color: rgb(255, 217, 140);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(0, 0, 0);")
        self.biomes_frame.setFrameShape(QFrame.StyledPanel)
        self.biomes_frame.setFrameShadow(QFrame.Raised)
        self.biomes_label = QLabel(self.biomes_frame)
        self.biomes_label.setObjectName(u"biomes_label")
        self.biomes_label.setGeometry(QRect(-1, 9, 271, 21))
        self.biomes_label.setFont(font1)
        self.biomes_label.setStyleSheet(u"")
        self.biomes_label.setAlignment(Qt.AlignCenter)
        self.biomes_label_3 = QLabel(self.biomes_frame)
        self.biomes_label_3.setObjectName(u"biomes_label_3")
        self.biomes_label_3.setGeometry(QRect(0, 40, 271, 21))
        self.biomes_label_3.setFont(font1)
        self.biomes_label_3.setStyleSheet(u"")
        self.biomes_label_3.setAlignment(Qt.AlignCenter)
        self.biomes_label_4 = QLabel(self.biomes_frame)
        self.biomes_label_4.setObjectName(u"biomes_label_4")
        self.biomes_label_4.setGeometry(QRect(0, 60, 271, 21))
        self.biomes_label_4.setFont(font1)
        self.biomes_label_4.setStyleSheet(u"")
        self.biomes_label_4.setAlignment(Qt.AlignCenter)
        self.biomes_label_5 = QLabel(self.biomes_frame)
        self.biomes_label_5.setObjectName(u"biomes_label_5")
        self.biomes_label_5.setGeometry(QRect(0, 80, 271, 21))
        self.biomes_label_5.setFont(font1)
        self.biomes_label_5.setStyleSheet(u"")
        self.biomes_label_5.setAlignment(Qt.AlignCenter)
        self.biomes_label_6 = QLabel(self.biomes_frame)
        self.biomes_label_6.setObjectName(u"biomes_label_6")
        self.biomes_label_6.setGeometry(QRect(10, 140, 251, 21))
        self.biomes_label_6.setFont(font1)
        self.biomes_label_6.setStyleSheet(u"")
        self.biomes_label_6.setPixmap(QPixmap(u"imgs/island_slice.png"))
        self.biomes_label_6.setScaledContents(True)
        self.biomes_label_6.setAlignment(Qt.AlignCenter)
        self.biomes_label_7 = QLabel(self.biomes_frame)
        self.biomes_label_7.setObjectName(u"biomes_label_7")
        self.biomes_label_7.setGeometry(QRect(10, 160, 251, 21))
        self.biomes_label_7.setFont(font1)
        self.biomes_label_7.setStyleSheet(u"")
        self.biomes_label_7.setPixmap(QPixmap(u"imgs/oasis_slice.png"))
        self.biomes_label_7.setScaledContents(True)
        self.biomes_label_7.setAlignment(Qt.AlignCenter)
        self.biomes_label_8 = QLabel(self.biomes_frame)
        self.biomes_label_8.setObjectName(u"biomes_label_8")
        self.biomes_label_8.setGeometry(QRect(10, 180, 251, 21))
        self.biomes_label_8.setFont(font1)
        self.biomes_label_8.setStyleSheet(u"")
        self.biomes_label_8.setPixmap(QPixmap(u"imgs/blossom_slice.png"))
        self.biomes_label_8.setScaledContents(True)
        self.biomes_label_8.setAlignment(Qt.AlignCenter)
        self.biomes_label_9 = QLabel(self.biomes_frame)
        self.biomes_label_9.setObjectName(u"biomes_label_9")
        self.biomes_label_9.setGeometry(QRect(10, 220, 251, 21))
        self.biomes_label_9.setFont(font1)
        self.biomes_label_9.setStyleSheet(u"")
        self.biomes_label_9.setPixmap(QPixmap(u"imgs/forest_slice.png"))
        self.biomes_label_9.setScaledContents(True)
        self.biomes_label_9.setAlignment(Qt.AlignCenter)
        self.biomes_label_10 = QLabel(self.biomes_frame)
        self.biomes_label_10.setObjectName(u"biomes_label_10")
        self.biomes_label_10.setGeometry(QRect(10, 200, 251, 21))
        self.biomes_label_10.setFont(font1)
        self.biomes_label_10.setStyleSheet(u"")
        self.biomes_label_10.setPixmap(QPixmap(u"imgs/caves_slice.png"))
        self.biomes_label_10.setScaledContents(True)
        self.biomes_label_10.setAlignment(Qt.AlignCenter)
        self.biomes_label_11 = QLabel(self.biomes_frame)
        self.biomes_label_11.setObjectName(u"biomes_label_11")
        self.biomes_label_11.setGeometry(QRect(10, 120, 251, 21))
        self.biomes_label_11.setFont(font1)
        self.biomes_label_11.setStyleSheet(u"")
        self.biomes_label_11.setPixmap(QPixmap(u"imgs/graylands_slice.png"))
        self.biomes_label_11.setScaledContents(True)
        self.biomes_label_11.setAlignment(Qt.AlignCenter)
        self.exit_button = QPushButton(self.ui_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(20, 600, 551, 31))
        # self.exit_button.clicked.connect(self.close)
        self.title_label = QLabel(self.ui_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(10, 9, 561, 51))
        font2 = QFont()
        font2.setFamily(u".AppleSystemUIFont")
        font2.setPointSize(39)
        self.title_label.setFont(font2)
        self.title_label.setStyleSheet(u"")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.retranslateAboutUi(ABOUT)

        QMetaObject.connectSlotsByName(ABOUT)

    # setupUi

    def retranslateAboutUi(self, ABOUT):
        ABOUT.setWindowTitle(QCoreApplication.translate("ABOUT", u"HOW TO USE", None))
        self.shape_label.setText(QCoreApplication.translate("ABOUT", u"SHAPE", None))
        self.shape_label_2.setText(QCoreApplication.translate("ABOUT", u"Adjust the size of the image", None))
        self.shape_label_3.setText(QCoreApplication.translate("ABOUT", u"Sizes are in pixels", None))
        self.shape_label_4.setText(QCoreApplication.translate("ABOUT", u"Length x Height", None))
        self.shape_label_5.setText("")
        self.shape_label_6.setText("")
        self.shape_label_7.setText("")
        self.scale_label.setText(QCoreApplication.translate("ABOUT", u"SCALE", None))
        self.scale_label_2.setText(QCoreApplication.translate("ABOUT", u"Adjust the zoom factor", None))
        self.scale_label_3.setText(QCoreApplication.translate("ABOUT", u"Smaller numbers are more zoomed-out", None))
        self.scale_label_4.setText(QCoreApplication.translate("ABOUT", u"Larger numbers are more zoomed-in", None))
        self.scale_label_5.setText("")
        self.scale_label_6.setText("")
        self.octaves_label.setText(QCoreApplication.translate("ABOUT", u"OCTAVES", None))
        self.octaves_label_2.setText(QCoreApplication.translate("ABOUT", u"Select amount of layers of detail", None))
        self.octaves_label_3.setText(QCoreApplication.translate("ABOUT", u"Low octaves produce smooth,  rounded", None))
        self.octaves_label_4.setText(
            QCoreApplication.translate("ABOUT", u"High octaves produce rigid,  detailed", None))
        self.octaves_label_5.setText("")
        self.octaves_label_6.setText("")
        self.biomes_label.setText(QCoreApplication.translate("ABOUT", u"BIOMES", None))
        self.biomes_label_3.setText(QCoreApplication.translate("ABOUT", u"Select the environment to generate", None))
        self.biomes_label_4.setText(
            QCoreApplication.translate("ABOUT", u"Gives the generator specific parameters", None))
        self.biomes_label_5.setText(QCoreApplication.translate("ABOUT", u"and colors to mimic terrains/regions", None))
        self.biomes_label_6.setText("")
        self.biomes_label_7.setText("")
        self.biomes_label_8.setText("")
        self.biomes_label_9.setText("")
        self.biomes_label_10.setText("")
        self.biomes_label_11.setText("")
        self.exit_button.setText(QCoreApplication.translate("ABOUT", u"Exit", None))
        self.title_label.setText(QCoreApplication.translate("ABOUT",
                                                            u"<html><head/><body><p><span style=\" font-style:italic;\">HOW TO USE</span></p></body></html>",
                                                            None))
    # retranslateUi


# Child class / Subclass to inherit and modify UI
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

        self.ui.exit_button.clicked.connect(self.close)