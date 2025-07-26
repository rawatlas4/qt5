from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from random import randint
import json
with open("daaa.json","r",encoding="utf-8") as file:
    data = json.load(file)

app = QApplication([])
    

window = QWidget()

label = QLabel("переможець")
vertical = QVBoxLayout()


label1 = QLabel("?")


button = QPushButton("натисни на мене")
def show_winner():
    winner = randint(1,100)
    label1.setText(str(winner))
    data.append(winner)
    with open("daaa.json","w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False)
button.clicked.connect(show_winner)
line  = QVBoxLayout()
line.addWidget(label,alignment = Qt.AlignCenter)
line.addWidget(label1,alignment = Qt.AlignCenter)
line.addWidget(button,alignment = Qt.AlignCenter)
window.setLayout(line)
def show_winner():
    winner = randint(1,100)
    winner = str(winner)



window.show()
window.setWindowTitle("Скебоб")
window.resize(500,700)


app.exec_()