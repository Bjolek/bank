
import requests
import json
import PyQt6
from PyQt6.QtWidgets import *

app = QApplication([])


window = QWidget()


Code_Сurrency = QLineEdit()
Date = QLineEdit()
Result = QLineEdit()

Сalculate = QPushButton("Обчислити")



mainLine = QVBoxLayout()

mainLine.addWidget(Code_Сurrency)
mainLine.addWidget(Date)
mainLine.addWidget(Result)
mainLine.addWidget(Сalculate)

window.setLayout(mainLine)

def get_valute():
    velcode = Code_Сurrency.text()
    date =  Result.text()
    a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={velcode}&date={date}&json")
    if a.status_code == 200:
        data = json.loads(a.text)
        (data[0]["txt"], data[0]["rate"])
    cur = 7
    Result.setText(str(cur))


Сalculate.clicked.connect(get_valute)


window.show()
app.exec()