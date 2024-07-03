import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout

class TextInputApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Contoh Aplikasi dengan Input Text dan Label')
        self.setGeometry(100, 100, 300, 200)

        # Membuat layout vertikal
        layout = QVBoxLayout()

        # Membuat input text
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText('Masukkan teks di sini')
        self.text_input.textChanged.connect(self.on_text_changed)

        # Membuat label
        self.label = QLabel('Teks yang dimasukkan akan muncul di sini')

        # Menambahkan input text dan label ke layout
        layout.addWidget(self.text_input)
        layout.addWidget(self.label)

        # Mengatur layout ke jendela
        self.setLayout(layout)

    def on_text_changed(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
window = TextInputApp()
window.show()
sys.exit(app.exec_())