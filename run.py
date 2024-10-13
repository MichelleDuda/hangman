import random

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
        newGame = input("Please input Y or N: ").upper()
        if newGame == "Y":
            print ("Great! Let's begin")
            word = get_word()
            play_game(word)
            break
        elif newGame == "N":
            print("Thanks for stopping by! We hope to see you again soon.")
            break
        else:
            print("Not a valid input. Please type Y or N")

def get_word():
    words = ['MONKEY', 'GUITAR', 'SCHOOL', 'GOAT', 'ELEPHANT', 'ZEBRA']
    word = random.choice(words)
    return word

def play_game(word):
    guesses = 6
    guessed_letters = []
    guessed_words = []
    print("_ " * len(word))
   
    while guesses > 0:
        guess = input("\nPlease choose a letter or word: ").upper()
        validate_input(guess)
        if not validate_input(guess):
            print ("Invalid data. Please enter only a single letter or a word.")

        if len(guess) == 1:
            if guess in guessed_letters:
                print(f'You already guessed {guess}. Please try again.\n')
            elif guess not in word:
                print(f'Sorry! {guess} is not in the word.')
                guessed_letters.append(guess)
                guesses -= 1
            else: 
                print(f'Congratulations. {guess} is in the word.')
                guessed_letters.append(guess)
                print(guessed_letters)

    

def validate_input(guess):
    if len(guess) == 1 and guess.isalpha():
        return True
    elif len(guess) > 1 and guess.isalpha():
        return True
    else:
        return False
        


def main():
    ''' 
    Calls functions for game to play
    '''
    welcome_screen()
    start_game()

main()