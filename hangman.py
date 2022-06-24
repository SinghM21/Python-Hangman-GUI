import random

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

    if word == word_list[word_amount - 1]:
        word = word + ' '

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

# Prompts and processes the guesses that the
# user makes
def guess(word):
    word = word.lower()
    duplicate_chars = 0
    guessed_word = '_' * (len(word) - 1)
    print("The word has {} characters".format(len(guessed_word)))
    
    # Find the number of duplicate characters
    for i in range(len(word) - 1):
        for j in range(i + 1, len(word) - 1):
            if word[i] == word[j]:
                duplicate_chars += 1
                break
   
    player_lives = 6
    letters_correct = 0
    # List of letters guessed
    letters_guessed = []

    # While the player still have lives
    while player_lives > 0:
        current_letters_correct = 0
        repeated_letters = 0
        guess = input("Enter a letter: ")
        guess = guess.lower()

        while len(guess) != 1:
            print("You can only enter a single character! ")
            guess = input("Enter a letter: ")
            guess = guess.lower()


        for x in range(len(word) - 1):
            if guess == word[x] and guess not in letters_guessed:
                current_letters_correct += 1
                letters_correct += 1
                letters_guessed.append(guess)
            elif guess in letters_guessed:
                repeated_letters += 1

        if player_lives == 0 or letters_correct == (len(word) - 1) - duplicate_chars:
            break

        elif current_letters_correct > 0:
            print("You guessed a letter correctly! Keep it up!")
            guessed_word = update_guessed_word(guessed_word, guess, word)
            print("The word now looks like", guessed_word)

        elif repeated_letters == len(word) - 1:
            print("You have already guessed this letter")
            print("You have guessed these letters {}".format(letters_guessed))

        elif current_letters_correct == 0:
            letters_guessed.append(guess)
            print("You guessed a wrong letter! Try again!")
            player_lives -= 1
            print("You now have {} lives".format(player_lives))
    
    if player_lives == 0:
        print("Game over, you lose!")
        print("The word was", word.lower())
    elif letters_correct == (len(word) - 1) - duplicate_chars:
        print("Congratulations! You guessed the word correctly!")
        print("You used these letters {} to guess the word: {}".format(letters_guessed, word))

def main():
    word_list = load_words()
    chosen_word = pick_word(word_list)
    guess(chosen_word)

if __name__ == "__main__":
    main()
