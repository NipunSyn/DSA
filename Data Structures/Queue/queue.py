from collections import deque

# implementation of queue datastructure


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def get_queue(self):
        return self.queue
