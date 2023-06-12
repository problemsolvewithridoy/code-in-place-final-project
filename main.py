# Please Subscribe my youtube channel "@problemsolvewithridoy"

"""
The WordGuess game where the player tries to guess a secret word by providing letter guesses.
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):
    """
    Plays the WordGuess game with the provided secret word.
    Args: secret_word (str): The word the player needs to guess.
    """
    guessed_word = ['-'] * len(secret_word)
    guesses_left = INITIAL_GUESSES

    while True:
        print('The word now looks like this:', ''.join(guessed_word))
        print('You have', guesses_left, 'guesses left')
        guess = input('Type a single letter here, then press enter: ').upper()

        if len(guess) != 1:
            print('Guess should only be a single character.')
            continue

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print('There are no', guess + "'s in the word")
            guesses_left -= 1

        if '-' not in guessed_word:
            print('Congratulations, the word is:', secret_word)
            break

        if guesses_left == 0:
            print('Sorry, you lost. The secret word was:', secret_word)
            break


def get_word():
    """
    Returns a secret word that the player is trying to guess in the game.
    The word is randomly selected from a list of words read from the file specified by LEXICON_FILE.
    Returns:
        str: The secret word.
    """
    with open(LEXICON_FILE, 'r') as file:
        word_list = file.read().splitlines()

    return random.choice(word_list)


def main():
    """
    The entry point of the program.
    Selects a secret word and starts the WordGuess game.
    """
    secret_word = get_word()
    play_game(secret_word)


if __name__ == "__main__":
    main()