import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QGridLayout
from Poczatkujac import Poczatkujacy_Window 
from test import Test_Window
import json
class wprowadzenie_Window(QMainWindow ):
    def __init__(self):
        super().__init__()
        
        self.label1 = QLabel("Wybierz")
        self.buttonPoczatkujacy = QPushButton("Początkujący")
        self.buttonPoczatkujacy.clicked.connect(self.buttonPoczatkujacy_clicked)

        self.buttonSprawdzenie = QPushButton("Doświadczenie z językiem")
        self.buttonSprawdzenie.clicked.connect(self.testjezyka)

        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        grid.addWidget(self.label1, 0, 1)
        grid.addWidget(self.buttonPoczatkujacy, 1, 1)
        grid.addWidget(self.buttonSprawdzenie, 1, 2)

        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)
        self.setWindowTitle("Wybór zaawansowania")
    def buttonPoczatkujacy_clicked(self):
        window = Poczatkujacy_Window()
        window.show()
    def testjezyka(self):   
        window = Test_Window()
        window.show()
            
app = QApplication(sys.argv)

# Ustaw arkusz stylów dla całej aplikacji
app.setStyleSheet("""
    QMainWindow {
        background-image: url(C:/Users/maciek/Desktop/duolingoapp/lonewolf.gif);
        background-position: center;
    }
""")

window = wprowadzenie_Window()
window.show()
app.exec()
