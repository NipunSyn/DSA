class BST:
    def __init__(self, data):
        # initializing the root node of the tree
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
            

        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements
    
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    def sum_of_elements(self):
        elements = self.in_order_traversal()
        return (sum(elements))

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

#       17
#      /  \  
#     4    20 
#    / \ 
#   1   9
#

tree = build_tree([17, 4, 1, 20, 9])
print("Tree Inorder: ", tree.in_order_traversal())
print("Tree Preorder: ", tree.pre_order_traversal())
print("Tree Postorder: ", tree.post_order_traversal())
tree.delete(4)
print("After deleting ",tree.in_order_traversal())