import random

def hangman():
    word_list = ["apple", "banana", "cherry", "grape", "orange", "melon", "peach"]

    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)
    attempts = 6  # მცდელობა
    guessed_letters = set()

    print("Welcome to the Hangman game!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"The letter '{guess}' is not in the word. Remaining attempts: {attempts}")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over. You lost.")
        print("The word was:", word)


if __name__ == "__main__":
    hangman()
