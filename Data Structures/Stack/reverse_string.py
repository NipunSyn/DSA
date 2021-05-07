from stack import Stack

#reversing string
def reverse(string):
    s = Stack()
    for c in string:
        s.push(c)
    
    new = ""
    for _ in range(len(s.get_stack())):
        new += s.pop()
    
    return new

print(reverse('hello'))