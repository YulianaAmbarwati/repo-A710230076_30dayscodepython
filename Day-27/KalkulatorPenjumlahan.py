import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator Penjumlahan")

        self.label1 = QLabel("Angka 1:")
        self.input1 = QLineEdit()
        self.label2 = QLabel("Angka 2:")
        self.input2 = QLineEdit()
        self.result_label = QLabel("Hasil: ")

        self.button = QPushButton("Tambah")
        self.button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def calculate(self):
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())
        result = num1 + num2
        self.result_label.setText(f"Hasil: {result}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()