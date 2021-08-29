import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:     # Else block is unnecessary because return would terminate function
        print("Please enter a valid number")


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
help(get_integer)
print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = get_integer(": ")

while guess != answer:
    if guess == 0:      # Can use multiple "if" statements
        print("You suck. Game over")
    elif guess < answer:
        print("Please try again and guess higher")
    else:
        print("Please try again and guess lower")
    guess = get_integer(": ")
print("Well done, you guessed it!")


# I JUST COMMENTED THIS OUT SO I COULD PRACTICE WHILE LOOPS

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed it")
# else:
# print("You got it the first time!")

# THIS IS INEFFICIENT CODE

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first try!")
