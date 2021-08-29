def fizz_buzz(n: int) -> str:
    """
    Count numbers in a sequence. However, if the number is
    divisible by 3, print "fizz".
    If divisible by 5, print "buzz".
    If divisible by 3 and 5, print "fizz buzz".

    :param n: The number to check.
    :return: The correct string in accordance with the game.
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return str(n)


input("Play Fizz Buzz!\nPress ENTER to start.")
print()

next_number = 0
while next_number < 100:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your turn: ")
    if player_answer != correct_answer:
        print("You lost. The correct answer was {}.".format(correct_answer))
        break
else:
    print("You did it you crazy sonofabitch, you reached {}".format(next_number))

# This was a student's solution that I really liked:

# number = 1
# # for number in range(1, 101):
# while number < 100:
#     computer_guess = fizz_buzz(number)
#     print("computer guessed: {}" .format(computer_guess))
#     number += 1
#     print("Your turn, enter the next value: ")
#     player_guess = str(input())
#     if player_guess == fizz_buzz(number):
#         # print("correct!")
#         pass
#     else:
#         print("incorrect value, game over")
#         break
#     number += 1


