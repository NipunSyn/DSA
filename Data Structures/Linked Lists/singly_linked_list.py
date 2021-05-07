# Class for node
# has data and pointer to next
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


# Class for the linked list 
class LinkedList:
    def __init__ (self):
        self.head = None
    
    #printing the elemets of the list, one by one    
    def print_list(self):
        
        current = self.head #pointer to iterate over the list
        while current is not None: #printing till the pointer points to null
            print(current.data)
            current = current.next #after printing, pointing to the next node
    
    #adding an element to the end of the list
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None: #if the list is empty
            self.head = new_node #pointing the head to the new node
            return
        
        #else
        last_node = self.head #initiating a pointer
        while last_node.next is not None: #traversing till last node is located
            last_node = last_node.next #break when last node reached
        last_node.next = new_node #make this point to the new node
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
    def insert_node_after(self, previous, data):

        if not previous: #checking if the previous node exists
            print("Previous node does not exist")
            return 
        
        new_node = Node(data)
        new_node.next = previous.next
        previous.next = new_node
    
    def delete_by_key(self, key):
        current = self.head #if the first node is to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None #initiate a pointer
        while current and current.data != key: 
            prev = current
            current = current.next
        
        if current is None:
            print("Key does not exist")
            return
    
        prev.next = current.next
        current = None
    
    def delete_by_index(self, position):
        current = self.head
        if position == 0:
            self.head = current.next
            current = None
            return
        
        prev = None
        index = 0
        while current and index != position:
            
            prev = current
            current = current.next
            index += 1
        
        if current is None:
            print("Position exceeds length of list")
            return
        
        prev.next = current.next
        current.next = None
        
    def length_iterative(self): ## iterative approach

        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count
    
    def length_recursive(self, node): ## recursive approach
        if node is None:
            return 0
        return 1 + self.length_r(node.next)
    
    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        prev1 = None
        current1 = self.head
        while current1 and current1.data != key1:
            prev1 = current1
            current1 = current1.next
        
        prev2 = None
        current2 = self.head
        while current2 and current2.data != key2:
            prev2 = current2
            current2 = current2.next
            
        if not current1 or not current2:
            print("One of the keys is not present in the list")
            return
        
        if prev1:
            prev1.next = current2
        else:
            self.head = current2
        if prev2:
            prev2.next = current1
        else:
            self.head = current1
        
        current1.next, current2.next = current2.next, current1.next
    
    def reverse_iterative(self): #iterative approach
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            return _reverse_recursive(current, prev)

        self.head = _reverse_recursive(current= self.head, prev= None)
            
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            
            else:
                s = q
                q = s.next
            
            new_head = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
    
    def remove_duplicates(self):
        current = self.head
        prev = None
        duplicates = dict()
        
        while current:
            #element already encountered
            if current.data in duplicates:
                prev.next = current.next
                current = None
            else:
                #element not encountered before
                duplicates[current.data] = 1
                prev = current
            current = prev.next
    
    #find nth to last node (n = 2 means second to last)
    def nth_from_last_method1(self, n):
        
        # Method 1:
        total_length = self.length_iterative()
        current = self.head
        while current:
            if total_length == n:
                return current.data
            
            total_length -= 1
            current = current.next
        
        if current is None:
            return None
        
    def nth_from_last_method2(self, n):
        # Method 2: Two Pointers
        #start with P pointing at head, Q n nodes ahead
        #when Q reaches Null, P will point to the required node
        
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            return None
        
        while p and q:
            p = p.next
            q = q.next
        return p.data
    
    def num_occurences_iterative(self, data):
        current = self.head
        if not current:
            return 0
        
        count = 0
        while current:
            if current.data == data:
                count += 1
            current = current.next
        
        return count 
                        
        
    def num_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.num_occurences_recursive(node.next, data)
        else:
            return self.num_occurences_recursive(node.next, data)
    
    def rotate_list_about_key(self, point):
        p = self.head
        q = self.head
        prev = None
        
        while p:
            if p.data == point:
                break
            p = p.next
            q = q.next
        if not p:
            return
        
        while q:
            prev = q
            q = q.next
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None
        
    def rotate_list_about_node(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None
    
    def is_palindrome1(self):
        # Method 1: pretty bad pretty bad. Not really using linked list
        
        s = ''
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1] 
    
    def is_palindrome2(self):    
        # Method 2: still pretty bad. Not using linked list :(
        
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        
        p = self.head
        while p:
            data = s.pop()
            if data != p.data:
                return False
            p = p.next
        return True
    
    def is_palindrome(self):
        # Method 3: finally gonna use two pointers
        p = self.head #points to the head
        q = self.head #points to the tail
        prev = [] #this list will store all the nodes for q (since we can't traverse in reverse)

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def move_tail_to_head(self):
        last = self.head
        second_last = None
        while last.next:
            second_last = last
            last = last.next
        last.next = self.head
        self.head = last
        second_last.next = None
    
    def sum_llists(self, llist):
        p = self.head
        q = llist.head
        
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            
            if not q:
                j = 0
            else:
                j = q.data
            
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s%10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
                
            if p:
                p = p.next
            if q:
                q = q.next
        
        sum_llist.print_list()
        

        
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# # llist.prepend("E")
# # llist.insert_node_after(llist.head.next, "F")
# # llist.delete_by_key("B")
# # llist.delete_by_index(1)
# # llist.print_list()
# # llist.swap_nodes("B", "D")
# # llist.print_list()
# # print(llist.length_iterative())
# # print((llist.length_recursive(llist.head)))
# # llist.reverse_iterative()
# llist.reverse_recursive()
# llist.print_list()

# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)

# llist1.merge_sorted(llist= llist2)
# llist1.print_list()

# llist1 = LinkedList()
# llist1.append(1)
# llist1.append(2)
# llist1.append(2)
# llist1.append(2)
# llist1.append(7)
# llist1.append(9)
# llist1.append(2)
# # llist1.append(10)
# # llist1.append(10)
# # llist1.append(10)

# # llist1.remove_duplicates()
# llist1.print_list()
# print()
# # print(llist1.nth_from_last_method2(2))


# print(llist1.num_occurences_iterative(2))
# print(llist1.num_occurences_recursive(llist1.head, 2))

# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
# llist.append(7)
# llist.print_list()
# print()
# llist.rotate_list_about_key(2)
# llist.print_list()
# print()
# llist.rotate_list_about_node(1)
# llist.print_list()

# llist = LinkedList()
# llist.append('r')
# llist.append('a')
# llist.append('c')
# llist.append('e')
# # llist.append('c')
# # llist.append('a')
# # llist.append('r')

# print(llist.is_palindrome())
# llist.move_tail_to_head()
# llist.print_list()

# llist1 = LinkedList()
# llist1.append(5)
# llist1.append(6)
# llist1.append(3)

# llist2 = LinkedList()
# llist2.append(8)
# llist2.append(4)
# llist2.append(2)

# llist1.sum_llists(llist2)

