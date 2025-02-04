class Node:
    """Defines a single node in a linked list."""
    def __init__(self, val):
        self.val = val  # Store character
        self.next = None  # Pointer to the next node

class MyLinkedList:
    """Custom singly linked list implementation."""
    def __init__(self):
        self.head = None  # First node in the list
        self.size = 0  # Number of elements in the list

    def add(self, c):
        """Appends a character to the linked list."""
        new_node = Node(c)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def swap_adjacent(self):
        """Swaps adjacent nodes directly without a dummy node."""
        if not self.head or not self.head.next:
            return  # If list has 0 or 1 elements, no swap needed

        # Swap first two nodes manually
        new_head = self.head.next
        prev = None
        curr = self.head

        while curr and curr.next:
            next_node = curr.next  # Second node in the pair
            curr.next = next_node.next  # Link first node to third node
            next_node.next = curr  # Swap the two nodes

            if prev:
                prev.next = next_node  # Connect previous pair to swapped pair

            prev = curr  # Move prev to current node
            curr = curr.next  # Move to the next pair

        self.head = new_head  # Update head pointer

    def to_string(self):
        """Converts linked list back to a string."""
        result = ""
        temp = self.head
        while temp:
            result += temp.val  # Append character to string
            temp = temp.next
        return result

def main():
    """Main function to take user input and swap adjacent characters."""
    user_input = input("Enter a string: ")  # Prompt user for input

    # Create linked list and populate it with characters
    my_list = MyLinkedList()
    for ch in user_input:
        my_list.add(ch)

    # Perform swap
    my_list.swap_adjacent()

    # Print swapped result
    print("Swapped Output:", my_list.to_string())

if __name__ == "__main__":
    main()