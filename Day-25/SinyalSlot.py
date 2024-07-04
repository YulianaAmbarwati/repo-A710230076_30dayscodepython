import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Signal and Slot Example')
        
        layout = QVBoxLayout()

        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_click)
        
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())