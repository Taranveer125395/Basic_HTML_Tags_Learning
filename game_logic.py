import random
from word_list import WORDS
from utils import get_guess, display_result

def play_game():
    word = random.choice(WORDS)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed_word:
        print("\nWord: ", " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters: ", ", ".join(sorted(guessed_letters)))

        guess = get_guess()
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
    
    display_result(word, guessed_word)

