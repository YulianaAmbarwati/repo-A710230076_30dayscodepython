import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hello World PyQt5')
        self.setGeometry(100, 100, 280, 80)

        label = QLabel('Hello, World!', self)
        label.setGeometry(10, 10, 260, 60)
        label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = HelloWorldWindow()
    window.show()

    sys.exit(app.exec_())