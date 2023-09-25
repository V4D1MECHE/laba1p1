import sys
import PyQt6 as Qt
import design
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QCoreApplication
from math import cos, sin, tan, pi

class App(design.Ui_Form, Qt.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    
def main():
    app = Qt.QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()