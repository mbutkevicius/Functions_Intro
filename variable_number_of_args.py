def sum_numbers(*numbers: float) -> float:
    """Find the sum of a variable amount of numbers."""
    result = 0
    for i in numbers:
        result += i
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))

# Oops, I messed up. I didn't write the code as concisely which I will do now.
# values = 1, 2, 3
# print(sum_numbers(*values))
#
# values = 8, 20, 2
# print(sum_numbers(*values))
#
# values = 12.5, 3.147, 98.1
# print(sum_numbers(*values))
#
# values = 1.1, 2.2, 5.5
# print(sum_numbers(*values))
