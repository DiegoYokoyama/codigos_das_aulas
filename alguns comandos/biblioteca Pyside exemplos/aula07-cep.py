import brazilcep 
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Buscar cep')
        
endereco = brazilcep.get_address_from_cep('79002000')
print(endereco)

'''app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec(app.exec_())'''
        