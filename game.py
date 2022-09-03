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
        # Pick word for hangman and create a line of underscores equal to word length
        self.word_list = hangman.load_words()
        self.chosen_word = hangman.pick_word(self.word_list)
        self.underscored_word = "_" * (len(self.chosen_word) - 1)

        # Create widgets
        self.blankword = QtWidgets.QLabel(self.underscored_word, alignment = QtCore.Qt.AlignCenter)
        self.hangman_image = QtWidgets.QLabel("", alignment = QtCore.Qt.AlignCenter)
        self.prompt = QtWidgets.QLabel("Enter a letter below: ", alignment = QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.edit = QLineEdit("", alignment = QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Submit")

        # Create layout and add widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.blankword)
        self.layout.addWidget(self.hangman_image)
        self.layout.addWidget(self.prompt)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)

        # On button click, execute guess function
        self.button.clicked.connect(self.guess_inputted)

    #Function to sanitize guess input and handle responses
    def guess_inputted(self):
        guess_string = str(self.edit.text())
        if (len(guess_string) != 1):
            self.prompt.setText("You can only submit one letter!")
            self.edit.setText("")
            
        else:
            result = hangman.process_guess(self.chosen_word, hangman.take_guess(self.edit.text()))
            self.edit.setText("")
            print(result)
            if (result == 1):
                self.underscored_word = hangman.update_guessed_word(self.underscored_word, guess_string, self.chosen_word)
                self.blankword.setText(self.underscored_word)
                self.prompt.setText("You guessed a letter correctly! Keep it up!")

            elif (result == 2):
                self.prompt.setText("You have already guessed this letter")

            elif (result == 3):
                self.prompt.setText("You guessed a wrong letter! Try again!")
            
            elif (result == 4):
                self.prompt.setText("Game over, you lose!")
            
            else:
                self.underscored_word = hangman.update_guessed_word(self.underscored_word, guess_string, self.chosen_word)
                self.blankword.setText(self.underscored_word)
                self.prompt.setText("Congratulations! You guessed the word correctly!")
    
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
