import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class NoteManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create text edit
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        
        # Create actions
        newAction = QAction(QIcon('new.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newNote)
        
        openAction = QAction(QIcon('open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openNote)
        
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveNote)
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        
        # Create menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        
        # Create toolbar
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(newAction)
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        
        # Set window properties
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Note Manager')
        self.show()
    
    def newNote(self):
        self.textEdit.clear()
    
    def openNote(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Note", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())
    
    def saveNote(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())
            QMessageBox.information(self, "Save Note", "Note saved successfully")

def main():
    app = QApplication(sys.argv)
    ex = NoteManager()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()