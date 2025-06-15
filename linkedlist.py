class Node:
    # Represents a single node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Handles list operations
    def __init__(self):
        self.head = None

    def append(self, data):
        # Add node at end
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        # Print all nodes
        temp = self.head
        result = []

        while temp:
            result.append(str(temp.data))
            temp = temp.next

        if result:
            print(" -> ".join(result))
        else:
            print("List is empty")

    def delete_nth_node(self, n):
        # Delete node at position n (starting from 1)
        if self.head is None:
            print("List is empty.")
            return

        if n <= 0:
            print("Invalid position.")
            return

        if n == 1:
            self.head = self.head.next
            return

        temp = self.head
        prev = None
        count = 1

        while temp and count < n:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range.")
            return

        prev.next = temp.next

def main():
    llist = LinkedList()

    while True:
        print("\nLinked List Operations:")
        print("1. Add a node")
        print("2. Delete a node")
        print("3. Print the list")
        print("4. Exit")

        ch = input("Enter your choice (1-4): ")

        if ch == "1":
            val = input("Enter the data to add: ")
            llist.append(val)
            print(f"Added {val} to the list.")

        elif ch == "2":
            try:
                pos = int(input("Enter the position to delete: "))
                llist.delete_nth_node(pos)
                print(f"Deleted node at position {pos}.")
            except:
                print("Invalid input.")

        elif ch == "3":
            print("\nCurrent Linked List:")
            llist.print_list()

        elif ch == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()