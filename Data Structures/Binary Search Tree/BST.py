class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        
    def print_tree(self, traversal_type):
        if traversal_type == "inorder":
            return self.inorder(self.root, "")
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root) #helper function
            
    def _insert(self, data, current_node):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        
        elif data > current_node.data:
            if not current_node.right:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        
        else:
            print("Value already present in tree")
    
    def search(self, data):
        if not self.root:
            return False
        is_found = self._search(self.root, data)
        return is_found
        
    def _search(self, current_node, data):
        if data < current_node.data:
            if current_node.left:
                return self._search(current_node.left, data)
            else:
                return False
        
        elif data > current_node.data:
            if current_node.right:
                return self._search(current_node.right, data)
            else:
                return False
        
        else:
            return True
    
    def inorder(self, start, traversal:str):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
        
    def find_max(self):
        if not self.root:
            return None
        
        else:
            maximum = self._find_max(self.root)
            return maximum
    
    def _find_max(self, current_node):
        if not current_node.right:
            return current_node.data
        return self._find_max(current_node.right)  
    
    def find_min(self):
        if not self.root:
            return None
        
        else:
            minimum = self._find_min(self.root)
            return minimum
    
    def _find_min(self, current_node):
        if not current_node.left:
            return current_node.data
        return self._find_min(current_node.left)  
    
    def delete(self, key):
        if not self.root:
            return
        else:
            self._delete(self.root, key)
            
    def _delete_exact(self, node, key):
        if not node.left:
            node.right = None
        elif not node.right:
            node.left = None
        if node.right.data == key:
            node.right = None
        if node.left.data == key:
            node.left = None
    
    def _delete(self, current_node, key):
        
        if key < current_node.data:
            if current_node.left:
                self._delete(current_node.left, key)
        elif key > current_node.data:
            if current_node.right:
                self._delete(current_node.right, key)
        
        
        else:
            if not current_node.left and not current_node.right:
                self._delete(current_node)
                return
            if not current_node.left:
                return current_node.right
            if not current_node.right:
                return current_node.left
            
            minimum = self._find_min(current_node.right)
            current_node.data = minimum
            current_node.right = self._delete(current_node.right, minimum)
            
        
#       23
#      /  \
#     7     77
#    /  \   /
#   3   14  36

bst = BST()
bst.insert(23)
bst.insert(7)
bst.insert(3)
bst.insert(14)
bst.insert(77)
bst.insert(36)
# print(bst.search(7))
print(bst.find_max())
print(bst.find_min())
print(bst.print_tree("inorder"))
bst.delete(3)
print(bst.print_tree("inorder"))