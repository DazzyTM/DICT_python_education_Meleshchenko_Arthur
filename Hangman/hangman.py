# Start

import random
import sys

print("HANGMAN""\nThe game will be available soon.")
a = 'start'
b = 'exit'
print("If you want to start the game type ""start")
print("If you want to quit the game type ""exit")
choice_input = (input(">"))
if choice_input == b:
    sys.exit("See you next time")

# Game

wordlist = 'python', 'java', 'javascript', 'php'
secret = random.choice(wordlist)
tries = 8
guesses = []
done = False

while not done:
    print('tries: ', tries)
    for letter in secret:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("-", end=" ")
    print("")

    guess = input("Input a letter:")
    guesses.append(guess.lower())
    if guess.lower() not in secret.lower():
        print("That letter doesn't appear in the word")
        tries -= 1
        if tries == 0:
            break

    done = True
    for letter in secret:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"You survived!")
else:
    print(f"Game over! The word was {secret}!")
