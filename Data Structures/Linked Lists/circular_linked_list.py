# more or less the same as singly linked lists
# the last node points to the head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node

        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head

        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        else:
            prev = None
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None

        if size == 1:
            return self.head

        mid = size//2
        count = 0
        prev = None
        current = self.head

        while current and count < mid:
            count += 1
            prev = current
            current = current.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while current.next != self.head:
            split_cllist.append(current.data)
            current = current.next
        split_cllist.append(current.data)

        self.print_list()
        print()
        split_cllist.print_list()

    def remove_node(self, node):
        if self.head == node:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        else:
            prev = None
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
                if current == node:
                    prev.next = current.next
                    current = current.next

    def josephus(self, step):
        """Function to solve the josephus problem. In this problem, step size is provided.
        And on every iteration, the node at the position corresponding to the step size is deleted.

        Args:
            step (int): The step size

        Returns:
            object: The data corresponding to the last remaining node is returned
        """

        current = self.head
        while len(self) > 1:
            count = 1  # counter to check the step size. When it equals the step size, the node is removed
            while count != step:
                current = current.next
                count += 1
            self.remove_node(current)
            current = current.next
        return current.data

    def is_circular(self, input_list):
        """Function to check whether a given linked list is a circular linked list

        Args:
            input_list (linked list ): Pass in the linked list that needs to be checked

        Returns:
            Bool: Returns a true, or false depending on whether the list is cyclic or not
        """
        current = input_list.head
        while current.next:  # checking for null
            current = current.next
            # if we encounter a node that points to the head, it is a circular list
            if current.next == input_list.head:
                return True
        return False  # otherwise, if we encounter Null, it is not a circular list


cl = CircularLinkedList()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.append(5)


print(cl.josephus(2))

# print(cl.is_circular(cl))
