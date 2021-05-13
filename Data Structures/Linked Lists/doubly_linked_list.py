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
        new_node.prev = prev
        new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
            new_node.next = None
            return
        self.head.prev = new_node
        new_node.prev = None
        new_node.next = self.head
        self.head = new_node

    def add_after_node(self, key, data):
        new_node = Node(data)
        if not self.head.next and self.head.data == key:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = None
            return
        current = self.head
        while current.next:
            if current.data == key:
                break
            current = current.next
        if not current.next and current.data != key:
            print('Key does not exist')
            return
        else:
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current

    def add_before_node(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# dll = DoublyLinkedList()
# dll.append(1)
# dll.add_after_node(1, 11)
# dll.append(2)
# dll.add_after_node(2, 12)
# dll.append(3)
# dll.add_before_node(3, 13)
# dll.append(4)
# dll.append(5)
# dll.prepend(0)
# dll.add_after_node(5, 6)
# dll.print_list()

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
