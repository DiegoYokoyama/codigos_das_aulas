import shutil 
import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from salvar_arquivo_ui import Ui_MainWindow

class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('organizador de arquivos')
        appIcon = QIcon()
        self.setWindowIcon(appIcon)
        self.btn_ok.clicked.connect(self.path)
        self.btn_organizar.clicked.connect(self.organizar)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str('pasta com arquivos'), '/home', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.txt_texto.path.setText(self.path)
        self.path = str