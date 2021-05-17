class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
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

bst = BST()
bst.insert(23)
bst.insert(7)
bst.insert(3)
bst.insert(14)
print(bst.search(7))