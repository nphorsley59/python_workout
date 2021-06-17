import random

def guessing_game():
    """This function is a number guessing game that takes user inputs and 
    provides basic feedback.
    """
    
    answer = random.randint(0, 10)
    first_guess = True
  
    while True:
        if first_guess:
            guess_as_string = input("What number am I thinking of? ")
            first_guess = False
        else:   
            guess_as_string = input("Try again: ")
        
        try:
            guess = int(guess_as_string)
        except ValueError:
            print("That's not a number!")
            continue
        
        if answer == guess:
            print("Correct!")
            break
        
        if answer > guess:
            print("Too low!")
            
        if answer < guess:
            print("Too high!")

guessing_game()