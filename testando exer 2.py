import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser

class Employee:
    def __init__(self, name, hours_worked, hourly_rate, additional_expense=0):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.additional_expense = additional_expense
    
    def calculate_payment(self):
        payment = self.hours_worked * self.hourly_rate
        return payment
    
    def __str__(self):
        return f"Name: {self.name}, Payment: {self.calculate_payment()}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Payment Calculator")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Enter employee data:")
        self.layout.addWidget(self.info_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.layout.addWidget(self.name_input)

        self.hours_input = QLineEdit()
        self.hours_input.setPlaceholderText("Hours Worked")
        self.layout.addWidget(self.hours_input)

        self.hourly_rate_input = QLineEdit()
        self.hourly_rate_input.setPlaceholderText("Hourly Rate")
        self.layout.addWidget(self.hourly_rate_input)

        self.additional_expense_input = QLineEdit()
        self.additional_expense_input.setPlaceholderText("Additional Expense (for outsourced employees)")
        self.layout.addWidget(self.additional_expense_input)

        self.add_button = QPushButton("Add Employee")
        self.add_button.clicked.connect(self.add_employee)
        self.layout.addWidget(self.add_button)

        self.display_text = QTextBrowser()
        self.layout.addWidget(self.display_text)

        self.central_widget.setLayout(self.layout)

        self.employees = []

    def add_employee(self):
        name = self.name_input.text()
        hours_worked = float(self.hours_input.text())
        hourly_rate = float(self.hourly_rate_input.text())
        additional_expense = float(self.additional_expense_input.text()) if self.additional_expense_input.text() else 0
        
        employee = Employee(name, hours_worked, hourly_rate, additional_expense)
        self.employees.append(employee)

        self.display_text.append(f"Employee added: {employee}")
        
        self.name_input.clear()
        self.hours_input.clear()
        self.hourly_rate_input.clear()
        self.additional_expense_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())