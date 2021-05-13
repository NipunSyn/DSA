class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        current = self.head
        if not current:
            self.head = new_node
            new_node.prev = None
            return

        prev = None
        while current:
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = current
        new_node.prev = None
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(6)
dll.print_list()
