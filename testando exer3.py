import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class Person:
    def __init__(self, name, income):
        self.name = name
        self.income = income

class Individual(Person):
    def __init__(self, name, income, health_expenses):
        super().__init__(name, income)
        self.health_expenses = health_expenses

    def calculate_tax(self):
        if self.income < 20000:
            tax = self.income * 0.15
        else:
            tax = self.income * 0.25
        
        if self.health_expenses > 0:
            tax -= self.health_expenses * 0.5
        
        return tax

class Company(Person):
    def __init__(self, name, income, num_employees):
        super().__init__(name, income)
        self.num_employees = num_employees

    def calculate_tax(self):
        if self.num_employees > 10:
            tax = self.income * 0.14
        else:
            tax = self.income * 0.16
        
        return tax

class TaxCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Impostos")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Informe os dados:")
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome")
        self.layout.addWidget(self.name_input)

        self.income_input = QLineEdit()
        self.income_input.setPlaceholderText("Renda Anual")
        self.layout.addWidget(self.income_input)

        self.expenses_input = QLineEdit()
        self.expenses_input.setPlaceholderText("Gastos com Saúde (se aplicável)")
        self.layout.addWidget(self.expenses_input)

        self.employees_input = QLineEdit()
        self.employees_input.setPlaceholderText("Número de Funcionários (se pessoa jurídica)")
        self.layout.addWidget(self.employees_input)

        self.calculate_button = QPushButton("Calcular Imposto")
        self.calculate_button.clicked.connect(self.calculate_tax)
        self.layout.addWidget(self.calculate_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        self.central_widget.setLayout(self.layout)

    def calculate_tax(self):
        name = self.name_input.text()
        income = float(self.income_input.text())
        expenses = float(self.expenses_input.text() if self.expenses_input.text() else 0)
        employees = int(self.employees_input.text() if self.employees_input.text() else 0)

        if expenses > 0:
            person = Individual(name, income, expenses)
        elif employees > 0:
            person = Company(name, income, employees)
        else:
            self.result_text.setPlainText("Preencha os dados corretamente.")
            return

        tax = person.calculate_tax()
        result = f"Imposto pago por {person.name}: R${tax:.2f}"
        self.result_text.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaxCalculatorApp()
    window.show()
    sys.exit(app.exec())