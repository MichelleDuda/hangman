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
            break
        elif newGame == "N":
            print("Thanks for stopping by! We hope to see you again soon.")
            break
        else:
            print("Not a valid input. Please type Y or N")
def main():
    ''' 
    Calls functions for game to play
    '''
    welcome_screen()
    start_game()

main()