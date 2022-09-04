import random

#Contains key information about the player
class GameStats:
    def __init__(self):
        self.player_lives = 6
        self.letters_guessed = []
        self.letters_correct = 0

    #Methods to retrieve and set values
    @property
    def lives(self):
        return self.player_lives

    @lives.setter
    def lives(self, a): 
        self.player_lives + a 

    @property
    def guessed(self):
        return self.letters_guessed
    
    @guessed.setter
    def guessed(self, b):
        self.letters_guessed.append(b)

    @property
    def correct(self):
        return self.letters_correct

    @correct.setter
    def correct(self, c):
        self.letters_correct + c

# Load the words from the word.txt file into an list
def load_words():
    word_list = []
    with open('words.txt') as word_file:
        for word in word_file:
            word_list.append(word)
        
    return word_list

# Pick a random word from the list
def pick_word(word_list):
    word_amount = len(word_list)
    random_num = random.randint(1, word_amount)
    word = word_list[random_num - 1]

    return word

# Update the hidden word covered by underscores 
# displayed to the user when they guess correctly
def update_guessed_word(current_word, character, word):
    previous_word_state = current_word
    char = character.lower()
    new_word_state = ""

    for x in range(len(previous_word_state)):
        if char == word[x]:
            new_word_state += char
        else:
            new_word_state += previous_word_state[x]
    
    return new_word_state

player = GameStats()

# Prompts and processes the guesses that the
# user makes
def take_guess(char):
    guess = char
    return guess

def process_guess(word, guessed_char):
    guess = guessed_char
    guess = guess.lower()
    word = word.lower()
    duplicate_chars = 0

    # Find the number of duplicate characters
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word) - 1):
            if word[i] == word[j]:
                duplicate_chars += 1
                break
    
    result = 0
    current_letters_correct = 0
    repeated_letters = 0

    #Check if guess is correct, or if a letter has already been guessed
    for x in range(len(word) - 1):
        if guess == word[x] and guess not in player.letters_guessed:
                current_letters_correct += 1
                player.letters_correct += 1
                player.letters_guessed.append(guess)
        elif guess in player.letters_guessed:
                repeated_letters += 1

    #Correct guess
    if current_letters_correct > 0:
        result = 1

    #Repeated guess
    elif repeated_letters == len(word) - 1:
        result = [2, guessed_char]

    #Wrong guess
    elif current_letters_correct == 0:
        player.letters_guessed.append(guess)
        player.player_lives -= 1
        result = [3, player.player_lives]
    
    #Player runs out of lives
    if player.player_lives == 0:
        result = [4, word.lower()]

    #Word is guessed
    elif player.letters_correct == (len(word) - 1) - duplicate_chars:
        result = [5, player.letters_guessed]

    return result

def main():
    word_list = load_words()
    chosen_word = pick_word(word_list)
    print("The word has {} characters".format(len(chosen_word)))

if __name__ == "__main__":
    main()
