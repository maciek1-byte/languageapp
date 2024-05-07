import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Wprowadzenie import wprowadzenie_Window
import json
class Wybor_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.bar = QProgressBar()
        self.bar.setValue(0)
        self.jezyk = None
        
        self.label1 = QLabel("Wybierz język")
        self.buttonAngielski = QPushButton('')
        self.buttonAngielski.clicked.connect(self.Angielski)
        self.buttonAngielski.setIcon(QIcon('eng.png'))
        
        self.buttonRosyjski = QPushButton('')
        self.buttonRosyjski.clicked.connect(self.Rosyjski)
        self.buttonRosyjski.setIcon(QIcon('flaga_rosji.webp'))
        
        self.buttonNiemiecki = QPushButton('')
        self.buttonNiemiecki.clicked.connect(self.Niemiecki)
        self.buttonNiemiecki.setIcon(QIcon('jezyk-niemiecki.jpg'))
        
        self.buttonWloski = QPushButton('')
        self.buttonWloski.clicked.connect(self.Wloski)
        self.buttonWloski.setIcon(QIcon('Wloski.jpg'))
        
        self.buttonFrancuski = QPushButton('')
        self.buttonFrancuski.clicked.connect(self.Francuski)
        self.buttonFrancuski.setIcon(QIcon('francuski.jpg'))
        
        self.buttonPotwierdzenie = QPushButton('Kontynuuj')
        self.buttonPotwierdzenie.clicked.connect(self.Potwierdzenie)
        
        grid = QGridLayout()
        grid.setSpacing(25)
        
        grid.addWidget(self.bar, 0, 2)
        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.buttonAngielski, 2, 0)
        grid.addWidget(self.buttonRosyjski, 2, 1)
        grid.addWidget(self.buttonNiemiecki, 3, 0)
        grid.addWidget(self.buttonWloski, 3, 1)
        grid.addWidget(self.buttonFrancuski, 4, 0)
        grid.addWidget(self.buttonPotwierdzenie, 5, 2)
        
        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)
        
        self.setWindowTitle("Wybór języka")
        
    def Angielski(self):
        self.bar.setValue(50)
        self.jezyk = "Angielski"
    
    def Rosyjski(self):
        self.bar.setValue(50)
        self.jezyk = "Rosyjski"
    
    def Niemiecki(self):
        self.bar.setValue(50)
        self.jezyk = "Niemiecki"
    
    def Wloski(self):
        self.bar.setValue(50)
        self.jezyk = "Wloski"
    
    def Francuski(self):
        self.bar.setValue(50)
        self.jezyk = "Francuski"
    def zapis_json(self):
        with open("zapis_jezyk.json", "w") as file:
            json.dump(self.jezyk, file)
        print("Zapisano")
    def Potwierdzenie(self):
        if self.jezyk:
            self.zapis_json()
            window = wprowadzenie_Window()
            window.show()
        else:
            QMessageBox.information(self, "Błąd", "Proszę wybrać język.")

app = QApplication(sys.argv)
window = Wybor_Window()
window.show()
app.exec()