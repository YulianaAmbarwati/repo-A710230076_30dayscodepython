import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTime, QTimer

class AlarmApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Alarm PyQt5')
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()

        self.time_label = QLabel('Setel Waktu Alarm:', self)
        layout.addWidget(self.time_label)

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat('HH:mm:ss')
        self.time_edit.setTime(QTime.currentTime())
        layout.addWidget(self.time_edit)

        self.set_alarm_button = QPushButton('Setel Alarm', self)
        self.set_alarm_button.clicked.connect(self.set_alarm)
        layout.addWidget(self.set_alarm_button)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_alarm)

    def set_alarm(self):
        self.alarm_time = self.time_edit.time()
        QMessageBox.information(self, 'Alarm Disetel', f'Alarm disetel untuk jam {self.alarm_time.toString("HH:mm:ss")}')
        self.timer.start(1000)

    def check_alarm(self):
        current_time = QTime.currentTime()
        if current_time >= self.alarm_time:
            self.timer.stop()
            QMessageBox.information(self, 'Alarm Berbunyi', 'Waktunya sekarang!')
            self.alarm_time = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlarmApp()
    ex.show()
    sys.exit(app.exec_())