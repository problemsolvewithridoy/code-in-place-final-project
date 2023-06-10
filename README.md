
# Stanford Code in Place Project - Final Project (The WordGuess game) 

This is one of several final project ideas. You can implement any of the final project ideas, or you can come up with your own. 

When the user plays WordGuess, the computer first selects a secret word at random from a list built into the program. The program then prints out a row of dashes—one for each letter in the secret word and asks the user to guess a letter. If the user guesses a letter that is in the word, the word is redisplayed with all instances of that letter shown in the correct positions, along with any letters correctly guessed on previous turns. If the letter does not appear in the word, the user is charged with an incorrect guess. The user keeps guessing letters until either (1) the user has correctly guessed all the letters in the word or (2) the user has made eight incorrect guesses. Two sample runs of the game are shown below (user input is shown in italics). 

The WordGuess game:- https://codeinplace.stanford.edu/cip3/share/LqW2pPXZIacSUhOTMY6I

let's start...............

To make this project you need to follow this step:-

## Deployment

To deploy this project run

```bash
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
```

## Image

![dsffsadf](https://github.com/problemsolvewithridoy/code-in-place-final-project/assets/123636419/0141e226-d41f-4c51-af02-668622fb0b71)


## You can follow me 

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

