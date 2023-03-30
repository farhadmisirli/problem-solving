"""
Palindrome Permutation:

Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)
"""


def solution(input_string: str) -> bool:
    char_frequency = {}

    for c in input_string.lower():
        if c != ' ':
            if c in char_frequency:
                char_frequency[c] += 1
            else:
                char_frequency[c] = 1

    odd_number_found = False
    for char, freq in char_frequency.items():
        if freq % 2 == 1:
            if odd_number_found:
                return False
            odd_number_found = True

    return True


example_input = "Tact Coa"
print(solution(example_input))
