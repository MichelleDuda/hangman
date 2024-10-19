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


def welcome_screen():
    ''' 
    Prints Welcome Screen
    '''
    print (r"""
      _    _                                          
     | |  | |                                         
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
     | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                          __/ |                       
                         |___/                        
    
    """)

    name = input("\nWelcome to Hangman! What's your name? ")
    print(f'\nHello {name}. Are you ready to start a new game of hangman?')

def start_game():
    ''' 
    Determines if a new game should commence
    '''
    
    while True:
        new_game = input("Please input Y or N: ").upper()
        if new_game == "Y":
            print ("Great! Let's begin")
            word = get_word()
            print (hangman_stages[6])
            print("_ " * len(word))
            play_game(word)
            break
        elif new_game == "N":
            print("Thanks for stopping by! We hope to see you again soon.")
            break
        else:
            print("Not a valid input. Please type Y or N")

def get_word():
    '''
    Randomly selects a word from the wordlist for the game
    '''
    words = ['MONKEY', 'GUITAR', 'SCHOOL', 'GOAT', 'ELEPHANT', 'ZEBRA']
    word = random.choice(words)
    return word

def play_game(word):
    '''
    Runs the main game loop for Hangman. The player guesses letters or words to try and 
    correctly identify the hidden word. The player has 6 incorrect guesses available 
    before losing the game.
    '''
    guesses = 6
    guessed_letters = []
    guessed_words = []
    word_completion = ["_" for _ in word]
    word_list=list(word)

  
    while guesses > 0:
        guess = input("\nPlease choose a letter or word: ").upper()
        validate_input(guess)
        if not validate_input(guess):
            print ("Invalid data. Please enter only a single letter or a word.")
        else:
            if len(guess) == 1:
                if guess in guessed_letters:
                    print(f'You already guessed {guess}. Please try again.\n')
                elif guess not in word:
                    print(f'Sorry! {guess} is not in the word.')
                    guessed_letters.append(guess)
                    guesses -= 1
                    print(hangman_stages[guesses])
                    print(word_completion)
                else: 
                    print(f'Congratulations. {guess} is in the word.')
                    guessed_letters.append(guess)
                    update_word_completion(guess, word_list, word_completion)
                    print(hangman_stages[guesses])
                    print(word_completion)

            if len(guess) > 1:
                if guess in guessed_words:
                    print(f'You already guessed {guess}. Please try again.\n')
                elif guess not in word:
                    print(f'Sorry! {guess} is incorrect. Please try again. ')
                    guessed_words.append(guess)
                    guesses -= 1
                else: 
                    print(f'Congratulations. {guess} is the word.')
                    guessed_words.append(guess)
                    print(guessed_words)

        if guesses == 0:
                print(f'\n\nGAME OVER!!! \nYou have run out of guesses. The correct word was {word}.')
                print("\nWould you like to play again (Y/N)")    

def validate_input(guess):
    '''
    Checks if the user's guess is either a letter or string of letters, containing no special characters or numbers
    '''
    if len(guess) == 1 and guess.isalpha():
        return True
    elif len(guess) > 1 and guess.isalpha():
        return True
    else:
        return False

def update_word_completion(guess, word_list, word_completion):
    ''' 
    Updates the word_completion variable with correctly guessed letters
    '''
    for i, letter in enumerate(word_list):
        if guess == letter:
            word_completion[i]=guess
    return word_completion
        
        


def main():
    ''' 
    Calls functions for game to play
    '''
    welcome_screen()
    start_game()

main()