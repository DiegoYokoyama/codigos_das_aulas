
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salvar_pasta.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 738)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_teste = QFrame(self.centralwidget)
        self.frame_teste.setObjectName(u"frame_teste")
        self.frame_teste.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame_teste.setFrameShape(QFrame.StyledPanel)
        self.frame_teste.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_teste)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_teste_2 = QFrame(self.frame_teste)
        self.frame_teste_2.setObjectName(u"frame_teste_2")
        self.frame_teste_2.setFrameShape(QFrame.StyledPanel)
        self.frame_teste_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_teste_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pasta = QLabel(self.frame_teste_2)
        self.lbl_pasta.setObjectName(u"lbl_pasta")

        self.verticalLayout.addWidget(self.lbl_pasta)

        self.btn_ok = QPushButton(self.frame_teste_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setCursor(QCursor(Qt.CrossCursor))
        self.btn_ok.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-top-right-radius:10px;")

        self.verticalLayout.addWidget(self.btn_ok)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.txt_texto = QLineEdit(self.frame_teste_2)
        self.txt_texto.setObjectName(u"texto")

        self.verticalLayout.addWidget(self.txt_texto)

        self.verticalSpacer = QSpacerItem(8, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_organizar = QPushButton(self.frame_teste_2)
        self.btn_organizar.setObjectName(u"btn_organizar")

        self.verticalLayout.addWidget(self.btn_organizar, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_teste_2)


        self.horizontalLayout_2.addWidget(self.frame_teste)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_pasta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/emai/icon arquivo.png\"/></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"selecione aqui", None))
        self.btn_organizar.setText(QCoreApplication.translate("MainWindow", u"organizar", None))
    # retranslateUi

