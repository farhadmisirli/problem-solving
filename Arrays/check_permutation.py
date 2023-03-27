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


a = "abc"
b = "bac"
print(solution_using_sorting(a, b))
