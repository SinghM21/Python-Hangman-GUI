import random

#Contains key information about the player
class GameStats:
    def __init__(self):
        self.player_lives = 6
        self.letters_guessed = []
        self.letters_correct = 0

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
    char = character
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

    for x in range(len(word) - 1):
        if guess == word[x] and guess not in player.letters_guessed:
                current_letters_correct += 1
                player.letters_correct += 1
                player.letters_guessed.append(guess)
        elif guess in player.letters_guessed:
                repeated_letters += 1

    if current_letters_correct > 0:
        print("You guessed a letter correctly! Keep it up!")
        result = 1

    elif repeated_letters == len(word) - 1:
        print("You have already guessed this letter")
        print("You have guessed these letters {}".format(player.letters_guessed))
        result = 2

    elif current_letters_correct == 0:
        player.letters_guessed.append(guess)
        print("You guessed a wrong letter! Try again!")
        player.player_lives -= 1
        print("You now have {} lives".format(player.player_lives))
        result = 3
    
    if player.player_lives == 0:
        print("Game over, you lose!")
        print("The word was", word.lower())
        result = 4

    elif player.letters_correct == (len(word) - 1) - duplicate_chars:
        print("Congratulations! You guessed the word correctly!")
        print("You used these letters {} to guess the word: {}".format(player.letters_guessed, word))
        result = 5

    return result

def main():
    word_list = load_words()
    chosen_word = pick_word(word_list)
    print("The word has {} characters".format(len(chosen_word)))

if __name__ == "__main__":
    main()
