# initialise a random int

# intialise a list of guesses to store the user's guesses

# ask the user for guesses

# add the user's guesses to the guesses list

# compare the guesses to the random int

# print COLDER or WARMER if the most recent guess is 10 numbers within the rand int

import random

def gen_random():
    return random.randint(1,100)

guesses = []

def user_guess():
    global guesses
    the_guess = int(input("Enter your guess here (1-100): "))
    guesses.append(the_guess)
    return the_guess

def compare_guess(the_guess, rand_int):
    global guesses
    if the_guess == rand_int:
        return "CORRECT"
    if len(guesses) == 1:
        if abs(the_guess - rand_int) <= 10:
            return "WARM"
        else:
            return "COLD"
    else:
        if abs(the_guess - rand_int) < abs(guesses[-2] - rand_int):
            return "WARMER"
        return "COLDER"

def replay():
    answer = ''
    while answer not in ['Y','N']:
        answer = input("Do you want to replay?(Y/N): ").upper()
    if answer == 'Y':
        return True
    return False

def play_on():
    game = True
    while game:
        rand_int = gen_random()
        global guesses
        guesses = []
        while True:
            user = user_guess()
            result = compare_guess(user, rand_int)
            print(result)
            if result == "CORRECT":
                print(f"You took {len(guesses)} guesses to get it!")
                break
        if not replay():
            game = False
            print("thanks for playing")

play_on()