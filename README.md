# <div align="center">Python Workout: 10 ten-minute exercises</div>

<br/>

### Exercise 1 - Number guessing game 
- Write a function that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
  * Too high
  * Too low
  * Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.

### My Solution
I didn't enjoy the user experience for the generic solution to this exercise. The first improvement I made was to catch non-numeric inputs with a try-except block.

{try-except image}

The second improvement I made was to give the "game master" parameters to customize. This included the upper and lower limit of the random integer as well as the number of attempts the user had to correctly guess the number. Note: this *technically* breaks the rules of the exercise

{docstring image}

View the full solution here {link to full solution}.

<br/>

### Exercise 2 - Summing numbers
