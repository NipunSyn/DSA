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

    def delete_key(self, key):
        current = self.head
        if not current.prev and not current.next and current.data == key:
            self.head = None
            return
        elif not current.prev and current.data == key:
            nxt = current.next
            nxt.prev = None
            self.head = nxt
            current.next = None
            return
        prev = None
        nxt = None
        while current.next:
            if current.data == key:
                break
            prev = current
            current = current.next
            nxt = current.next
        if not current.next and current.data == key:
            prev.next = None
            current.prev = None
            return
        elif current.data == key:
            prev.next = current.next
            nxt.prev = current.prev
            current.next = None
            current.prev = None
            return

    def delete_node(self, node):
        current = self.head
        while current:
            if current == node and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return

                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return

            elif current == node:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return

                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def reverse_list(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        current = self.head
        seen = dict()
        while current:
            if current.data not in seen:
                seen[current.data] = 1
                current = current.next
            else:
                nxt = current.next
                self.delete_node(current)
                current = nxt

    def pairs_with_sum(self, sum_value):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_value:
                    pairs.append(f"({p.data}, {q.data})")
                q = q.next
            p = p.next
        return pairs

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

# dll = DoublyLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.append(4)
# dll.append(5)
# # dll.delete_key(4)
# dll.reverse_list()
# dll.print_list()

# dll = DoublyLinkedList()
# dll.append(8)
# dll.append(8)
# dll.append(4)
# dll.append(4)
# dll.append(6)
# dll.append(4)
# dll.append(9)
# dll.append(6)
# dll.append(10)
# dll.append(11)
# dll.remove_duplicates()
# dll.print_list()

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print(dll.pairs_with_sum(9))
