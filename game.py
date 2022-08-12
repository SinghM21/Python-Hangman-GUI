import random
import sys
from tkinter import Widget
import hangman
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QLineEdit, QPushButton, QDialog)

# Class for GUI handling
class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Create widgets
        self.text = QtWidgets.QLabel("No letter entered", alignment = QtCore.Qt.AlignCenter)
        self.prompt = QtWidgets.QLabel("Enter a letter below: ", alignment = QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.edit = QLineEdit("", alignment = QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Submit")

        # Create layout and add widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.prompt)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)

        # On button click, execute guess function
        self.button.clicked.connect(self.guess_inputted)

    def guess_inputted(self):
        guess_string = str(self.edit.text())
        guess_length = (len(guess_string))
        if (guess_length != 1):
            self.prompt.setText("You can only submit one letter!")
        else:
            hangman.take_guess(self.edit.text())
    
def main():

    # Create window constraints, then display window
    app = QtWidgets.QApplication([])
    widget = MyApp()
    widget.setWindowTitle("Hangman")
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
