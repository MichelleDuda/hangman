import random

hangman_stages = [
    r"""
    +---------+
    |         |
    |         O
    |        \|/
    |        / \
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |         O
    |        \|/
    |        /
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |         O
    |        \|/
    |
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |         O
    |        \|
    |
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |         O
    |         |
    |
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |         O
    |
    |
    |
    |
    ---
    """,
    r"""
    +---------+
    |         |
    |
    |
    |
    |
    |
    ---
    """
]


def text_color(color_code, text):
    '''
    Apply ANSI color codes to text

    '''
    return f'\033[{color_code}m{text}\033[0m'


def welcome_screen():
    '''
    Prints Welcome Screen & Instructions
    '''
    print(r"""
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/
    """)

    name = input("\n\nWelcome to Hangman! What's your name?\n")
    print(f'\nHello {name}.')

    while True:
        instructions = input(
            "Would you like to view the game instructions? Enter Y or N:\n"
        ).upper()
        if instructions == "Y":
            print(r"""
            ----------------------------------------------------------------------
            ----------------------------------------------------------------------

                                        How To Play

            Guess the secret word before the stick figure man is hung from the
            gallows.

            Enter a letter to see if it is in the word. If the guess is correct
            the corresponding blank slot will be filled with the letter. If the
            guess is wrong, a new peice of the stick figure man will be drawn.

            You have 6 lives until the drawing is complete & you lose the game.

            Do your best to save the man....

            ----------------------------------------------------------------------
            ----------------------------------------------------------------------
            """)
            break
        elif instructions == "N":
            break
        else:
            print(text_color(
                "31",
                f"\nSorry! {instructions.upper()} is not a valid input. "
                "Please type Y or N"
            ))


def start_game():
    '''
    Determines if a new game should commence
    '''
    while True:
        new_game = input(
            f'\nAre you ready to start a new game of hangman? Please input '
            f"{text_color('34', 'Y')} or {text_color('34', 'N')}:\n"
        ).upper()
        if new_game == "Y":
            print("\nGreat! Let's begin")
            word = get_word()
            print(hangman_stages[6])
            print("_ " * len(word))
            play_game(word)
            break
        elif new_game == "N":
            print("Thanks for stopping by! We hope to see you again soon.")
            break
        else:
            print(text_color(
                "31",
                f"\nSorry! {new_game.upper()} is not a valid input."
                "Please type Y or N."
            ))


def get_word():
    '''
    Randomly selects a word from the wordlist for the game
    '''
    words = {
        '1': [
            'CAMP', 'BARK', 'MOON', 'FIRE', 'CORN',
            'WOLF', 'SHIP', 'TREE', 'FOOD', 'BANK',
            'WIND', 'SNOW', 'DUCK', 'BOOK', 'FISH',
            'ROAD', 'HILL', 'ROCK', 'STAR', 'GOLD'
        ],
        '2': [
            'TRAIN', 'SHARK', 'PEACH', 'CLOUD', 'BREAD',
            'SNAKE', 'LIGHT', 'STAGE', 'BRICK', 'HORSE',
            'BRAIN', 'DRIVE', 'PIZZA', 'CRANE', 'FLUTE',
            'GRAPE', 'SMILE', 'TOAST', 'WORLD', 'CYCLE'
        ],
        '3': [
            'PLANET', 'JUNGLE', 'ROCKET', 'GARDEN', 'SILENT',
            'MOBILE', 'BRIDGE', 'FARMER', 'MARKET', 'MOUNTA',
            'DESERT', 'PIRATE', 'STREAM', 'BOTTLE', 'SCHOOL',
            'ISLAND', 'SUMMER', 'SPIDER', 'KITTEN', 'STREET'
        ]
    }

    while True:
        difficulty = input(
            'Please select your difficulty level:\n\n'
            '1. Easy\n2. Medium\n3. Hard\n\n'
            'Enter 1, 2 or 3 accordingly:\n'
            )
        if difficulty in words:
            return random.choice(words[difficulty])
        else:
            print(text_color(
                "31",
                f'\nSorry! {difficulty.upper()} is not A valid option.'
                " Please enter 1, 2, or 3."
                ))


def play_game(word):
    '''
    Runs the main game loop for Hangman.
    Player guesses letters or words to try and correctly identify
    the hidden word. There are 6 incorrect guesses available
    before losing the game.
    '''
    guesses = 6
    guessed_letters = []
    guessed_words = []
    word_completion = ["_" for _ in word]
    word_list = list(word)
    word_complete = False

    while guesses > 0 and not word_complete:
        print(f'You have {text_color("1;38", guesses)} guesses remaining!')
        print(f"Guessed Letters: {' '.join(guessed_letters)}")
        print(f"Guessed Words: {' '.join(guessed_words)}")
        guess = input("\nPlease choose a letter or word:\n").upper()
        validate_input(word, guess)
        if not validate_input(word, guess):
            print(text_color(
                "31",
                f"Invalid data. Please enter only a single letter or a word"
                f" containing {len(word)} characters.\n"))
        else:
            if len(guess) == 1:
                if guess in guessed_letters:
                    print(text_color(
                        "31",
                        f'You already guessed {guess}. Please try again.\n'
                    ))
                elif guess not in word:
                    guessed_letters.append(guess)
                    guesses -= 1
                    print(hangman_stages[guesses])
                    print(f"Word: {' '.join(word_completion)}")
                    print(text_color(
                        "31",
                        f'Sorry! {guess} is not in the word.\n'
                    ))
                    word_complete = check_word_completion(word_completion)
                else:
                    guessed_letters.append(guess)
                    update_word_completion(guess, word_list, word_completion)
                    print(hangman_stages[guesses])
                    print(f"Word: {' '.join(word_completion)}")
                    print(text_color(
                        "32",
                        f'Congratulations. {guess} is in the word.\n'
                    ))
                    word_complete = check_word_completion(word_completion)

            if len(guess) > 1:
                if guess in guessed_words:
                    print(text_color(
                        "31",
                        f'You already guessed {guess}. Please try again.\n'
                    ))
                elif guess != word:
                    guessed_words.append(guess)
                    guesses -= 1
                    print(hangman_stages[guesses])
                    print(f"Word: {' '.join(word_completion)}")
                    print(text_color(
                        "31",
                        f'Sorry! {guess} is incorrect. Please try again.\n'
                    ))
                else:
                    print(hangman_stages[guesses])
                    word_completion = list(guess)
                    print(f"Word: {' '.join(word_completion)}")
                    guessed_words.append(guess)
                    word_complete = check_word_completion(word_completion)

        if guesses == 0:
            print(text_color(
                "1;31",
                f'GAME OVER!!! \nYou have run out of guesses. '
                f'The correct word was {word}.'
            ))

    if word_complete:
        print(text_color(
            "1;32",
            f'CONGRATULATIONS! YOU WIN!! The word is {word}!'
        ))
    restart_game()


def validate_input(word, guess):
    '''
    Checks if the user's guess is either a letter or string of letters
    equal to the length of the word, containing no special characters
    or numbers
    '''
    return guess.isalpha() and (len(guess) == 1 or len(guess) == len(word))


def update_word_completion(guess, word_list, word_completion):
    '''
    Updates the word_completion variable with correctly guessed letters
    '''
    for i, letter in enumerate(word_list):
        if guess == letter:
            word_completion[i] = guess
    return word_completion


def check_word_completion(word_completion):
    '''
    Checks if the word is complete after a letter or word is guessed
    '''
    if "_" in word_completion:
        return False
    else:
        return True


def restart_game():
    '''
    Determines if a new game should commence
    '''
    print("\nWould you like to play again (Y/N)")
    while True:
        new_game = input("Please input Y or N:\n").upper()
        if new_game == "Y":
            print("Great! Let's begin")
            word = get_word()
            print(hangman_stages[6])
            print("_ " * len(word))
            play_game(word)
            break
        elif new_game == "N":
            print("Thanks for stopping by! We hope to see you again soon.")
            break
        else:
            print(text_color("31", "Not a valid input. Please type Y or N"))


def main():
    '''
    Calls functions for game to play
    '''
    welcome_screen()
    start_game()


main()
