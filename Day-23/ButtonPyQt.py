import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Membuat tombol
        btn = QPushButton('Click Me', self)
        btn.clicked.connect(self.showMessage)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        self.setLayout(vbox)

        # Konfigurasi jendela
        self.setWindowTitle('PyQt5 Button Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showMessage(self):
        # Menampilkan pesan saat tombol ditekan
        QMessageBox.information(self, 'Message', 'Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())