import sys
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(528, 461)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_tituloprincipal = QLabel(self.centralwidget)
        self.lbl_tituloprincipal.setObjectName(u"lbl_tituloprincipal")
        font = QFont()
        font.setPointSize(15)
        self.lbl_tituloprincipal.setFont(font)

        self.verticalLayout.addWidget(self.lbl_tituloprincipal)

        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")
        font1 = QFont()
        font1.setPointSize(21)
        self.btn_ok.setFont(font1)

        self.verticalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font1)

        self.verticalLayout.addWidget(self.btn_cancel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_tituloprincipal.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
    # retranslateUi
    
app = QApplication(sys.argv)
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec()

