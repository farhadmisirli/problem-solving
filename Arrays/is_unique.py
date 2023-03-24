# Time complexity of our algorithm depends on sorting algorithm.
# Most of the sorting algorithms works for  O(nlog(n)) time.
def solution_using_sorting(word: str) -> bool:
    word_arr = list(word)
    word_arr.sort()

    for i in range(1, len(word_arr)):
        if word_arr[i] == word_arr[i - 1]:
            return False

    return True


# This solution works for 0(n2) time.
# We are comparing every character of the string to every other character of the string
def brute_force_solution(word: str) -> bool:
    n = len(word)

    for i in range(n):
        for j in range(n):
            if i != j and word[i] == word[j]:
                return False

    return True


example = "abca"
print(solution_using_sorting(example))
print(brute_force_solution(example))
