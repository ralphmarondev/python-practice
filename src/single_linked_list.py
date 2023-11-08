# single linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_specific_position(self, data, pos):
        if pos < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return

        current_node = self.head
        for _ in range(pos - 1):
            if current_node is None:
                print("Position exceeds the length of the list")
                return
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def delete_last(self):
        if self.head is None:
            print("List is empty, Nothing to delete.")
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def delete_first(self):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return

        self.head = self.head.next

    def delete_at_pos(self, pos):
        if pos < 0:
            print("Invalid position")
            return

        if self.is_empty():
            print("List is empty. Nothing to delete")
            return

        if pos == 0:
            self.head = self.head.next
            return

        current_node = self.head
        for _ in range(pos - 1):
            if current_node is None or current_node.next is None:
                print("Position exceeds the length of the list.")
                return
            current_node = current_node.next

        current_node.next = current_node.next.next

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end="-> ")
            current_node = current_node.next
        print("bye")


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(1)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(2)

    linked_list.display()
    linked_list.insert_at_beginning(0)

    linked_list.display()

    linked_list.insert_at_specific_position(3.5, 2)
    linked_list.display()

    linked_list.delete_last()
    linked_list.display()

    linked_list.delete_first()
    linked_list.display()

    linked_list.delete_at_pos(2)
    linked_list.display()
