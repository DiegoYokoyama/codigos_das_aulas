# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_usuario.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_login = QFrame(self.centralwidget)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setStyleSheet(u"background-color: rgb(26, 37, 255);")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_usuario = QFrame(self.frame_login)
        self.frame_usuario.setObjectName(u"frame_usuario")
        self.frame_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_usuario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_usuario = QLabel(self.frame_usuario)
        self.lbl_usuario.setObjectName(u"lbl_usuario")

        self.verticalLayout_2.addWidget(self.lbl_usuario)

        self.lbl_foto = QLabel(self.frame_usuario)
        self.lbl_foto.setObjectName(u"lbl_foto")
        self.lbl_foto.setPixmap(QPixmap(u":/icon/animal-dog.png"))
        self.lbl_foto.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.lbl_foto)

        self.btn_usuario = QLineEdit(self.frame_usuario)
        self.btn_usuario.setObjectName(u"btn_usuario")

        self.verticalLayout_2.addWidget(self.btn_usuario)


        self.verticalLayout_3.addWidget(self.frame_usuario)

        self.frame_senha = QFrame(self.frame_login)
        self.frame_senha.setObjectName(u"frame_senha")
        self.frame_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_senha = QLabel(self.frame_senha)
        self.lbl_senha.setObjectName(u"lbl_senha")

        self.verticalLayout.addWidget(self.lbl_senha)

        self.btn_senha = QLineEdit(self.frame_senha)
        self.btn_senha.setObjectName(u"btn_senha")
        self.btn_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.btn_senha)


        self.verticalLayout_3.addWidget(self.frame_senha)


        self.verticalLayout_4.addWidget(self.frame_login)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Usuario</span></p></body></html>", None))
        self.lbl_foto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/animal-dog.png\"/><img src=\":/icon/animal-dog.png\"/><img src=\":/icon/animal-dog.png\"/></p></body></html>", None))
        self.btn_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu texto", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Senha</span></p></body></html>", None))
        self.btn_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu texto", None))
    # retranslateUi

