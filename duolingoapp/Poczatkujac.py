import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QGridLayout

class Poczatkujacy_Window(QMainWindow):
    def __init___(self):
        super().__init__()
        self.buttonSlowo = QPushButton("Tutaj znajdzie się słówko")
        self.buttonSlowo.clicked.connect(self.buttonSlowo_clicked)
        
        self.buttonZapamietales = QPushButton("Zapamietałeś?")
        self.buttonZapamietales.clicked.connect(self.buttonZapamietales_clicked)
        
        self.buttonZapomniales = QPushButton("Zapomniałeś?")
        self.buttonZapomniales.clicked.connect(self.buttonZapomniales_clicked)
        
        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(self.buttonSlowo)
        grid.addWidget(self.buttonZapomniales)
        grid.addWidget(self.buttonZapamietales)
        
        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)
        self.setWindowTitle("Nauka słówek")
    def Slowka(self):
        with open("angielskislowa", "r") as file:
            for line in file:
                    
    def buttonSlowo_clicked(self):
        
app = QApplication(sys.argv)
window = Poczatkujacy_Window()
window.show()
app.exec()        