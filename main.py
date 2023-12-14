from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton 
class Calculator(QWidget): 
    def init(self): 
        self.block()
    def block(self):
        self.setWindowTitle('калькулятор')
        self.setGeometry(100,100, 500, 500)
        self.init()
        a = QVBoxLayout() 
        b = QHBoxLayout() 

