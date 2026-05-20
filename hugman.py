import random

WORD_LIST = [
    "python",
    "hangman",
    "computer",
    "programming",
    "keyboard",
    "science",
    "elephant",
    "mountain"
]

HANGMAN_STAGES = [
    """
  -----
  |   |
      |
      |
      |
      |
=========
    """,
    """
  -----
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  -----
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  -----
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  -----
  |   |
  O   |
 /|\\  |
      |
      |
=========
    """,
    """
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
    """,
    """
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
    """
]


def display_word(word, guessed_letters):

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


def check_win(word, guessed_letters):

    for letter in word:
        if letter not in guessed_letters:
            return False

    return True


def play_hangman():

    print("=" * 40)
    print("      Welcome to HANGMAN GAME!")
    print("=" * 40)

    word = random.choice(WORD_LIST)

    guessed_letters = []

    wrong_guesses = 0
    max_wrong = 6

    print(f"\nThe word has {len(word)} letters.\n")

    while wrong_guesses < max_wrong:

        print(HANGMAN_STAGES[wrong_guesses])

        print(f"Word: {display_word(word, guessed_letters)}")

        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        else:
            print("Guessed letters: None")

        print(f"Attempts left: {max_wrong - wrong_guesses}")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only!\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is NOT in the word!\n")

        if check_win(word, guessed_letters):

            print(HANGMAN_STAGES[wrong_guesses])

            print(f"Word: {display_word(word, guessed_letters)}")

            print("\nCongratulations! You WON!")
            print(f"The word was: '{word}'")

            return

    print(HANGMAN_STAGES[wrong_guesses])

    print("\nGAME OVER! You lost.")
    print(f"The word was: '{word}'")


def main():

    while True:

        play_hangman()

        again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower().strip()

        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
