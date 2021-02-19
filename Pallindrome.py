import numpy as np
import re


def is_this_pallindrome(sentence, space):
    """Function to detect given sentence is pallindrome or not.
    This takes sentence as an input
    it takes two arguments
    sentence and space

    ex: is_this_pallindrome('ABCBA, 'YES')"""
    input_sentence = str.upper(sentence)
    char_list = []
    result = ""
    # checks if we have any spaces
    if str.upper(space) == "YES":
        char_list = list(re.sub(r"\s+", "", input_sentence))
    else:
        char_list = list(input_sentence)
    # print(int(len(char_list)/2))
    length_str = len(char_list)
    # print(length_str % 2)
    left_to_right = 0
    right_to_left = 0
    mid_point = int(len(char_list) / 2)

    if len(char_list) % 2 == 0:
        # left to right till middle
        left_to_right = np.array(char_list[0:mid_point])
        # right to left till middle
        right_to_left = np.array(char_list[mid_point:length_str])
    else:
        # left to right till middle
        left_to_right = np.array(char_list[0:mid_point])
        # right to left till middle
        right_to_left = np.array(char_list[mid_point + 1 : length_str])

    # comparing two arrays
    comparison = left_to_right == right_to_left[::-1]
    if comparison.all() == True:
        result = "it is pallindrome"
    else:
        result = "nope! not a pallindrome"

    return result


if __name__ == "__main__":
    text = input("Enter text : ")
    print("chacking if {} is pallindrome".format(text))
    print(is_this_pallindrome(text, "no"))
