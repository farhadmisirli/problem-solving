"""
String Compression:

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3
"""


def solution(input_string: str) -> str:
    compressed_string = []
    count = 0
    for i in range(len(input_string)):
        count += 1
        if i + 1 >= len(input_string) or input_string[i + 1] != input_string[i]:
            compressed_string.append(input_string[i])
            compressed_string.append(str(count))
            count = 0

    return "".join(compressed_string)


example_input = "aabcccccaaa"
print(solution(example_input))
