import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import json
class Test_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.labelPytanie = QLabel("Tutaj znajdzie się pytanie")
        self.opcjaA = QCheckBox("Odpowiedz A")
        self.opcjaB = QCheckBox("Odpowiedz B")
        self.opcjaC = QCheckBox("Odpowiedz C")
        self.potwierdzenie = QPushButton("Potwierdz")
        self.potwierdzenie.clicked.connect(self.sprawdzenie)
        self.label2 = QLabel()
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelPytanie)
        self.layout.addWidget(self.opcjaA)
        self.layout.addWidget(self.opcjaB)
        self.layout.addWidget(self.opcjaC)
        self.layout.addWidget(self.potwierdzenie)
        self.layout.addWidget(self.label2)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.setWindowTitle("Pytanie")
    def jazyk(self):
        jezyk = None 
        with open("zapis_jezyk.json", 'r') as file:
            jezyk = json.load(file)
    def pytania(self):
        linijka = 0
        if self.jezyk == "Angielski":
            with open("englishTest.txt", "r") as file:
                for line in file:
                    print(line)
                    linijka +=1
                    #if linijka <=50:
                        #if linijka 
    def sprawdzenie(self):
        self.jazyk()
        self.pytania()
app = QApplication(sys.argv)
window = Test_Window()
window.show()
app.exec()    