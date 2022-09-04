from ctypes import alignment
import sys
import hangman
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtWidgets import QLineEdit, QLabel

# Class for GUI handling
class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Pick word for hangman and create a line of underscores equal to word length
        self.word_list = hangman.load_words()
        self.chosen_word = hangman.pick_word(self.word_list)
        self.underscored_word = "_" * (len(self.chosen_word) - 1)

        #Gets initial lives and converts it into a string
        self.lives = hangman.GameStats().player_lives
        self.lives_counter = "Lives: " + str(self.lives)

        # Create widgets
        self.lives_remaining = QtWidgets.QLabel(self.lives_counter, alignment = QtCore.Qt.AlignCenter)
        self.amount_of_characters = QtWidgets.QLabel("The word has {} characters".format(len(self.chosen_word) - 1), alignment = QtCore.Qt.AlignCenter)
        self.blankword = QtWidgets.QLabel(self.underscored_word, alignment = QtCore.Qt.AlignCenter)
        self.prompt = QtWidgets.QLabel("Enter a letter below: ", alignment = QtCore.Qt.AlignBottom | QtCore.Qt.AlignCenter)
        self.edit = QLineEdit("", alignment = QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Submit")
        self.image = QtWidgets.QLabel(alignment = QtCore.Qt.AlignCenter)
        self.image.setPixmap(QPixmap('Images/hangman_6.png').scaled(90, 108))

        # Create layout and add widgets
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.lives_remaining)
        self.layout.addWidget(self.amount_of_characters)
        self.layout.addWidget(self.blankword)
        self.layout.addWidget(self.image)
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
            
        else:
            result = hangman.process_guess(self.chosen_word, hangman.take_guess(self.edit.text()))
            self.edit.setText("")
            print(result)
            if (result == 1):
                self.underscored_word = hangman.update_guessed_word(self.underscored_word, guess_string, self.chosen_word)
                self.blankword.setText(self.underscored_word)
                self.prompt.setText("You guessed a letter correctly! Keep it up!")

            elif (result[0] == 2):
                self.prompt.setText("You have already guessed the letter '{}'".format(result[1]))

            elif (result[0] == 3):
                self.prompt.setText("You guessed a wrong letter! Try again!")
                self.lives_counter = "Lives: " + str(result[1])
                self.lives_remaining.setText(self.lives_counter)
                select_image = 'Images/hangman_' + str(result[1])
                self.image.setPixmap(QPixmap(select_image).scaled(90, 108))
            
            elif (result[0] == 4):
                self.prompt.setText("Game over, you lose! The word was {}".format(result[1]))
                self.lives_counter = "Lives: " + str(0)
                self.lives_remaining.setText(self.lives_counter)
                self.image.setPixmap(QPixmap('Images/hangman_0').scaled(90, 108))
            
            else:
                self.underscored_word = hangman.update_guessed_word(self.underscored_word, guess_string, self.chosen_word)
                self.blankword.setText(self.underscored_word)
                self.prompt.setText("Congratulations! You guessed the word correctly using these characters! {}".format(result[1]))

        #Clear text from guess field after every guess
        self.edit.setText("")
    
def main():
    # Create window constraints, then display window
    app = QtWidgets.QApplication([])
    widget = MyApp()
    widget.setWindowTitle("Hangman")
    widget.setWindowIcon(QIcon('Images/hangman_0.png'))
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
