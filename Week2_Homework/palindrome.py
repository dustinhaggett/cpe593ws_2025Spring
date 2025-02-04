import re

# Node class for linked list
class Node:
    def __init__(self, char):
        self.char = char
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, char):
        """Adds a new character to the linked list"""
        if not self.head:
            self.head = Node(char)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(char)

    def build_reversed(self):
        """Creates a reversed linked list"""
        reversed_list = LinkedList()
        current = self.head
        while current:
            new_node = Node(current.char)
            new_node.next = reversed_list.head
            reversed_list.head = new_node
            current = current.next
        return reversed_list

    def compare(self, other):
        """Compares two linked lists"""
        a, b = self.head, other.head
        while a and b:
            if a.char != b.char:
                return False
            a, b = a.next, b.next
        return a is None and b is None  # Ensure both lists end together

# Function to check palindrome
def is_palindrome(s):
    # Step 1: Preprocess input (remove non-letters, convert to lowercase)
    cleaned = re.sub(r'[^a-zA-Z]', '', s).lower()

    # Step 2: Build linked list
    ll = LinkedList()
    for char in cleaned:
        ll.append(char)

    # Step 3: Create reversed linked list and compare
    reversed_ll = ll.build_reversed()

    return ll.compare(reversed_ll)

# Test
test_cases = ["Taco cat", "I Love DSA", "A man, a plan, a canal, Panama!", "racecar", "1234abcdDCBA4321"]

for case in test_cases:
    result = is_palindrome(case)
    print(f"'{case}' -> {'Palindrome' if result else 'Not a Palindrome'}")