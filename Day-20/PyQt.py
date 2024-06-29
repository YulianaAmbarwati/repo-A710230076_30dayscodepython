import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Label dan Tombol")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Halo, PyQt5!", self)
        self.label.move(100, 100)
        
        self.button = QPushButton("Klik Saya", self)
        self.button.move(100, 150)
        self.button.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        self.label.setText("Tombol Diklik!")
        self.label.adjustSize()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())