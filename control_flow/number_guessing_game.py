# using a while, illustrates it's a ongoing input so the user has to guess it right before it ends. a if statement is
# normally used within a while loop, so that if the user does a lower or higher than the guess, it can give the user
# a message and the loop can be going until they guess right.

# Random is a built-in function which is used when you want randomize numbers
import random
number = (random.randint(1, 20))
# guess is a variable,
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# using a loop
while number != guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("Enter guess between 1 and 20: "))
        guess_count += 1
    else:
        out_of_guesses = True
        print("you ran of guesses, you lose")
    if guess < number:
        print("your guess is too low")
    elif guess > number:
        print("your guess is too high")
    if guess == number:
        print("you won")

# first counter i came across, was the loop was ever going, either too low or too high so i had to add