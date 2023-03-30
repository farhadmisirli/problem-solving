"""
String Rotation:

Assume you have a method isSubstring() which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of" erbottlewat").
"""


# if you concat s1s1 u will get waterbottlewaterbottle. and if u look more carefully you will see s2 inside it )
# just think a little to solve the problem
def is_rotation(s1: str, s2: str) -> bool:
    # if one is rotation of another then their length must be same
    if len(s1) != len(s2):
        return False

    return is_substring(s1 + s1, s2)


# assume that this method already provided
def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2 or s2 in s1


print(is_rotation("waterbottle", "erbottlewat"))
