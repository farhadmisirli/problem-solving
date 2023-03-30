"""
Check Permutation

Given two strings, write a method to decide if one is a permutation of the other
Example: abc is permutation of bac
"""


def solution_using_sorting(a: str, b: str) -> bool:
    # return False if the length of strings is different
    if len(a) < len(b):
        return False

    # If lengths are same then sort the strings and compare
    sorted_a = "".join(sorted(a))
    sorted_b = "".join(sorted(b))

    return sorted_a == sorted_b


def solution_using_characters_count(a: str, b: str) -> bool:
    # return False if the length of strings is different
    if len(a) < len(b):
        return False

    char_count_dict = {}

    for c in a:
        if c in char_count_dict:
            char_count_dict[c] += 1
        else:
            char_count_dict[c] = 1

    for c in b:
        if c in char_count_dict:
            char_count_dict[c] -= 1
        else:
            return False

    # check char_count_dict. if char counts are same, value of your count_dic will be 0
    for key, count in char_count_dict.items():
        if count != 0:
            return False

    return True


a = "abc"
b = "bac"
print(solution_using_sorting(a, b))
print(solution_using_characters_count(a, b))
