import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class LaptopSpecsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout utama
        vbox = QVBoxLayout()

        # Layout untuk input
        input_layout = QVBoxLayout()
        
        self.brand_label = QLabel('Brand:', self)
        self.brand_input = QLineEdit(self)
        input_layout.addWidget(self.brand_label)
        input_layout.addWidget(self.brand_input)
        
        self.model_label = QLabel('Model:', self)
        self.model_input = QLineEdit(self)
        input_layout.addWidget(self.model_label)
        input_layout.addWidget(self.model_input)
        
        self.processor_label = QLabel('Processor:', self)
        self.processor_input = QLineEdit(self)
        input_layout.addWidget(self.processor_label)
        input_layout.addWidget(self.processor_input)
        
        self.ram_label = QLabel('RAM (GB):', self)
        self.ram_input = QLineEdit(self)
        input_layout.addWidget(self.ram_label)
        input_layout.addWidget(self.ram_input)
        
        self.storage_label = QLabel('Storage (GB):', self)
        self.storage_input = QLineEdit(self)
        input_layout.addWidget(self.storage_label)
        input_layout.addWidget(self.storage_input)
        
        self.add_button = QPushButton('Add Laptop', self)
        self.add_button.clicked.connect(self.add_laptop)
        input_layout.addWidget(self.add_button)

        # Layout untuk daftar spesifikasi
        self.specs_list = QTextEdit(self)
        self.specs_list.setReadOnly(True)
        
        vbox.addLayout(input_layout)
        vbox.addWidget(self.specs_list)

        # Mengatur layout utama
        self.setLayout(vbox)

        # Pengaturan jendela
        self.setWindowTitle('Laptop Specifications')
        self.setGeometry(100, 100, 400, 400)

    def add_laptop(self):
        brand = self.brand_input.text()
        model = self.model_input.text()
        processor = self.processor_input.text()
        ram = self.ram_input.text()
        storage = self.storage_input.text()

        if brand and model and processor and ram and storage:
            spec = f"Brand: {brand}\nModel: {model}\nProcessor: {processor}\nRAM: {ram} GB\nStorage: {storage} GB\n"
            self.specs_list.append(spec)
            
            # Mengosongkan input setelah ditambahkan
            self.brand_input.clear()
            self.model_input.clear()
            self.processor_input.clear()
            self.ram_input.clear()
            self.storage_input.clear()
        else:
            self.specs_list.append("Please fill in all fields!\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LaptopSpecsApp()
    window.show()
    sys.exit(app.exec_())