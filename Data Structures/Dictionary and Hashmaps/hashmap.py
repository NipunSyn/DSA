class HashTable:  
    def __init__(self):
        self.MAXIMUM = 100
        self.arr = [None for i in range(self.MAXIMUM)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAXIMUM
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None