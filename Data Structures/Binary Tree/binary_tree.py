from collections import deque

# Queue is required for BFS or level order traversal
class Queue(object):
    def __init__ (self):
        self.buffer = deque()
    
    def enqueue(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.buffer[-1].value
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.buffer)
    
# Stack is required for reverse level order traversal
class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1].value
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.stack)


# Node for binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# Binary tree implementation as a class
class BinaryTree(object):
    """          1
               /   /
             2       3
            / \      / /
            4  5     6  7

TYPES OF TRAVERSALS
1) Depth First Search:
1.a) Preorder
1.b) Inorder
2.c) Postorder
2) Level Order Search
3) Reverse Level Order Search

    Args:
        object (int, string): The value to be added to the root node
    """
    
    def __init__ (self, root):
        self.root = Node(root) #create a node with the value root, to make it the root
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        
        elif traversal_type == "levelorder":
            return self.levelorder(tree.root)
        
        elif traversal_type == "reverselevelorder":
            return self.reverselevelorder(tree.root)
        
        else:
            return "Not a valid traversal type"
    
    def preorder(self, start, traversal:str):
        """1.a) Preorder: Go to the node, print it, move left till and do the same till the node is None. Then move right. here 1-2-4-5-3-6-7-8
        
        Root -> Left -> Right

        Args:
            start (starting node): Node where the traversal starts
            traversal (str): The path that is traversed

        Returns:
            [str]: Final path traversed
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal:str):
        """1.b) Inorder: Go to all the left nodes, print them. Print the middle node, then move to the right nodes. here 4-2-5-1-6-3-7
        
        Left -> Root -> Right

        Args:
            start (starting node): Node where the traversal starts
            traversal (str): The path that is traversed

        Returns:
            str: Final path traversed
        """
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal:str):
        """1.c) Postorder: Go to all the left nodes, print them. Then go to all the right nodes, print them. Then print the middle node. here 4-5-2-6-7-3-1
        
        Left -> Right -> Root

        Args:
            start (starting node): Node where the traversal starts
            traversal (str): The path that is traversed

        Returns:
            str: Final path traversed
        """
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def levelorder(self, start):
        """Also known as Breadth First Seach. All the elements at a given level will be printed from left to right. Followed, by the next level, and so on.
        
        here 1-2-3-4-5-6-7

        Args:
            start (starting node): Node where the traversal starts
        """
        
        if not start:
            return
        
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            traversal += (str(queue.peek()) + "-")
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
        
    def reverselevelorder(self, start):
        """Similar to reverse order traversal, just that the elements at the leaves are printed first, and the root node at the end. here 4-5-6-7-2-3-1

        Args:
            start (starting node): Node where the traversal starts

        Returns:
            str: Final path traversed
        """
        if not start:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            
            #here we check the right node first
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        
        return traversal
        

tree = BinaryTree(1)
tree.root.left = Node(2)            
tree.root.right = Node(3)           
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))



