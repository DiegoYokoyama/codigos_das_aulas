from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
from circle import Circle
from square import Square

class ShapeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Áreas")
        self.layout = QVBoxLayout()

        self.input_layout = QHBoxLayout()
        self.input_label = QLabel("Raio/ Lado:")
        self.input_field = QLineEdit()
        
        self.shape_type_label = QLabel("Tipo (circle/square):")
        self.shape_type_field = QLineEdit()
        self.color_label = QLabel("Cor:")
        self.color_field = QLineEdit()  # Campo para a cor da figura
        
        self.input_layout.addWidget(self.input_label)
        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.shape_type_label)
        self.input_layout.addWidget(self.shape_type_field)
        self.input_layout.addWidget(self.color_label)
        self.input_layout.addWidget(self.color_field)

        self.calculate_button = QPushButton("Calcular Área")
        self.result_display = QTextBrowser()

        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_display)
        self.setLayout(self.layout)

        self.calculate_button.clicked.connect(self.calculate_area)

    def calculate_area(self):
        input_value = float(self.input_field.text())
        shape_type = self.shape_type_field.text()
        color = self.color_field.text()  # Obtendo a cor da figura

        if shape_type == "circle":
            shape = Circle(input_value, color)
        elif shape_type == "square":
            shape = Square(input_value, color)
        else:
            self.result_display.append("Tipo de forma inválido.")
            return

        area = shape.calculate_area()
        self.result_display.append(f"Área calculada da figura {shape_type} ({color}): {area}")

if __name__ == "__main__":
    app = QApplication([])
    window = ShapeApp()
    window.show()
    app.exec_()
