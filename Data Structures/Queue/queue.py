from collections import deque

class Queue:
    def __init__ (self):
        self.buffer = deque()
        
    def enqueue(self, item):
        self.buffer.appendleft(item)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def get_queue(self):
        return self.buffer
        
    