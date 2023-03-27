# Time complexity of our algorithm depends on sorting algorithm.
# Note that! Most of the sorting algorithms works for O(nlog(n)) time.
def solution_using_sorting(word: str) -> bool:
    word_arr = list(word)
    word_arr.sort()

    for i in range(1, len(word_arr)):
        if word_arr[i] == word_arr[i - 1]:
            return False

    return True


# We are comparing every character of the string to every other character of the string
# This solution works for 0(n2) time.
def brute_force_solution(word: str) -> bool:
    n = len(word)

    for i in range(n):
        for j in range(n):
            if i != j and word[i] == word[j]:
                return False

    return True


# In this solution we used Dictionary to store frequency of each character.
# Dictionary insertion and retrieval takes O(1) time on average.
def solution_using_dictionary(word: str) -> bool:
    n = len(word)
    freq_arr = {}

    for i in range(n):
        if word[i] not in freq_arr:
            freq_arr[word[i]] = 1
        else:
            return False

    return True


input_str = "aba"
print(solution_using_sorting(input_str))
print(brute_force_solution(input_str))
print(solution_using_dictionary(input_str))
