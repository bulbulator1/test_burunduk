from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                            QLabel, QPushButton,
                            QVBoxLayout)

app = QApplication([])
window = QWidget()
window.show()
window.setWindowTitle("Определить победителя")
window.resize(400,200)

click = QPushButton("Сгенерировать")
label = QLabel("Победитель:")
num = QLabel("?")

v_line = QVBoxLayout()
v_line.addWidget(label)
v_line.addWidget(num)
v_line.addWidget(click)
window.setLayout(v_line)


app.exec_()