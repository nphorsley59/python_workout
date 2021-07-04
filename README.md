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
I built upon the generic solution to this game because I felt like the user experience was lacking. The first improvement I made was to catch non-numeric inputs with a try-except block. <br/>

![alt_text](https://github.com/nphorsley59/python_workout/blob/main/images/E1_try-except.png "try-except block")

The second improvement I made was to give the "game master" parameters to customize. This included the upper and lower limit of the random integer as well as the number of attempts the user had to correctly guess the number. Note: this *technically* breaks the rules of the exercise, but the added replay value more than makes up for it.  <br/>

![alt_text](https://github.com/nphorsley59/python_workout/blob/main/images/E1_docstring.png "docstring")

View the full solution [here](https://github.com/nphorsley59/python_workout/blob/main/workouts/workout1.py).

<br/>

### Exercise 2 - Summing numbers
- Write a function that does the same thing as the built-in sum function.
- Instead of taking a single sequence as a parameter, it should take a variable number of arguments.
- Using the built-in sum function is not allowed.

### My Solution
Writing a solution to the base requirements of this exercise was pretty straight-forward. By prefixing a function parameter with \*, it can accept any number of arguments. For fun, I recreated the sum() function exactly (it accepts two parameters, an iterable and a starting point).

![alt_text](https://github.com/nphorsley59/python_workout/blob/main/images/E2_sum.png "sum")

I also put it to use in a simple counting task.

![alt_text](https://github.com/nphorsley59/python_workout/blob/main/images/E2_counting.png "counting")

View the full solution [here]().

<br/>
