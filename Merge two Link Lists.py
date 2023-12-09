class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy
    count = 0  # Variable to keep track of the number of nodes

    while list1 is not None and list2 is not None and count < 50:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        count += 1

    # If one of the lists is not exhausted, append the remaining nodes
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

# Function to print a linked list without "None" and the arrow after the last number
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end="")
        current = current.next
        if current:
            print(">", end="")
    print()

# Function to create a linked list from user input
def create_linked_list_from_input():
    values = input("Enter space-separated values for the linked list: ").split()
    values = [int(val) for val in values]
    values = values[:50]  # Ensure the number of nodes is in the range [0, 50]

    dummy = ListNode()
    current = dummy

    for val in values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

# Example usage:
# Creating two sorted linked lists from user input
print("Enter values for the first sorted linked list:")
list1 = create_linked_list_from_input()

print("Enter values for the second sorted linked list:")
list2 = create_linked_list_from_input()

# Merging the sorted linked lists
merged_list = merge_sorted_lists(list1, list2)

# Printing the merged linked list without "None" and the arrow after the last number
print("\nMerged List:")
print_linked_list(merged_list)