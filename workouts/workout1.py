import random

def guessing_game():
    """This function is a number guessing game that takes user inputs and 
    provides basic feedback.
    """
    
    answer = random.randint(0, 10)
    first_guess = True
  
    while True:
        guess_as_string = guess_prompt(first_guess)
        
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

def guess_prompt(first_guess):
    """This function determines which prompt to give the user, depending on 
    whether or not it is their first guess.

    Args:
        first_guess ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    if first_guess:
        guess_as_string = input("What number am I thinking of? ")
        first_guess = False
    else:   
        guess_as_string = input("Try again: ")
    
    return guess_as_string;

guessing_game()