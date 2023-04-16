"""
Remove Duplicates

Write code to remove duplicates from an unsorted linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# solution takes O(N) time, where N is the number of elements in the linked list.
def solution_using_temporary_buffer(node):
    prev = None
    freq_dict = set()

    while node:
        if node.data in freq_dict:
            prev.next = node.next
        else:
            freq_dict.add(node.data)
            prev = node

        node = node.next


def print_linked_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next


head = Node(5)
head.next = Node(3)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(1)

solution_using_temporary_buffer(head)

print_linked_list(head)
