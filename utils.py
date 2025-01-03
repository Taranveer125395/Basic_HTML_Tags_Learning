def display_welcome():
    print("Welcome to the Guess the Word Game!")
    print("Try to guess the word one letter at a time.")
    print("You have 6 attempts. Good luck!")

def get_guess():
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def display_result(word, guessed_word):
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)
