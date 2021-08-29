def factorial(n: int) -> int:
    """
    Calculates the factorial of a number using a for loop.
    :param n: the `int` to get the factorial from.
    :return: The factorial of `n`
    """
    if n == 0:
        return 1
    result = 1
    for f in range(n, 1, -1):
        result *= f
    return result


for i in range(36):
    print(i, factorial(i))

# Okay so not going to lie this shit confused the shit out of me.
# I don't know if I just need to let this digest but these functions
# are killing me.
# This was the instructor's solution: I copied somebody else's homework.

# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
#
#     return result
#
#
# for i in range(36):
#     print(i, factorial(i))
