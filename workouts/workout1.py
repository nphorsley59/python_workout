import random

def guessing_game(lower_limit: int = 1, upper_limit: int = 10, 
                  guesses_allowed: int = 5):
    """A number guessing game that takes user inputs and provides basic 
        feedback.
    
    Args:
        lower_limit (int, optional): Lower limit of randomly generated number.
        upper_limit (int, optional): Upper limit of randomly generated number.
        guesses_allowed (int, optional): Maximum number of guesses allowed per 
            game.
        
    """
    print("Welcome to the Number Guessing Game! I am thinking a number "
        f"between {lower_limit} and {upper_limit}.")
    answer = random.randint(lower_limit, upper_limit)
    guess_count = 1
  
    while guess_count <= guesses_allowed:
        prompt = generate_prompt(guess_count, guesses_allowed)
        guess_as_string = input(prompt)
        
        try:
            guess = int(guess_as_string)
        except ValueError:
            print("That's not a number!")
            continue
        
        if answer == guess:
            print("Correct!")
            break
        
        if answer > guess:
            print("Too low...")
            
        if answer < guess:
            print("Too high...")
        
        guess_count += 1
    
    if answer != guess:
        print("Better luck next time!")


def generate_prompt(guess_count: int, guesses_allowed: int) -> str:
    """Generates the correct prompt for the user.

    Args:
        guess_count (int): Current guess count.
        guesses_allowed (int): Number of guesses allowed.

    Returns:
        prompt (str): Correct prompt for the user.
        
    """
    
    if guess_count == 1:
        prompt = "What number am I thinking of? "
    elif guess_count == guesses_allowed:
        prompt = "This is your final guess. Good luck! " 
    else:
        guesses_remaining = guesses_allowed - guess_count + 1
        prompt = f"Try again! You have {guesses_remaining} guesses remaining. "
    
    return prompt;


guessing_game()