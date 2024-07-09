import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout Utama
        mainLayout = QVBoxLayout()

        # Input Celcius
        self.celsiusLabel = QLabel('Celcius:', self)
        self.celsiusInput = QLineEdit(self)

        # Tombol Konversi
        self.convertButton = QPushButton('Convert', self)
        self.convertButton.clicked.connect(self.convertTemperature)

        # Output Fahrenheit dan Kelvin
        self.fahrenheitLabel = QLabel('Fahrenheit: ', self)
        self.kelvinLabel = QLabel('Kelvin: ', self)

        # Menambahkan widget ke layout
        mainLayout.addWidget(self.celsiusLabel)
        mainLayout.addWidget(self.celsiusInput)
        mainLayout.addWidget(self.convertButton)
        mainLayout.addWidget(self.fahrenheitLabel)
        mainLayout.addWidget(self.kelvinLabel)

        self.setLayout(mainLayout)

        # Pengaturan jendela
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def convertTemperature(self):
        try:
            celsius = float(self.celsiusInput.text())
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15

            self.fahrenheitLabel.setText(f'Fahrenheit: {fahrenheit:.2f}')
            self.kelvinLabel.setText(f'Kelvin: {kelvin:.2f}')
        except ValueError:
            self.fahrenheitLabel.setText('Fahrenheit: Invalid input')
            self.kelvinLabel.setText('Kelvin: Invalid input')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TemperatureConverter()
    sys.exit(app.exec_())