def multiply(x: float, y: float) -> float:
    """
    Multiply two `int` values.

    :param x: First `int` value.
    :param y: The `int` to multiply x by.
    :return: The product of the two factors.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Index word backwards and forwards to determine
    if the string is a palindrome.

    :param string: The string the function checks when
    determining if it's a palindrome.
    :return: The Boolean value of the palindrome.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check whether sentence is a palindrome.

    The function only checks alphanumeric values and
    ignores everything else.

    :param sentence: The sentence to check.
    :return: The Boolean value of palindrome.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


answer = multiply(18, 3)
print(answer)

p = palindrome_sentence()
# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome sentence"
#           .format(sentence))
# else:
#     print("'{}' is not a palindrome sentence"
#           .format(sentence))
#
# print()
#
# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

