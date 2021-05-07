from stack import Stack

#decimal to binary
def binary(x):
    s = Stack()
    while x > 0:
        remainder = x%2
        s.push(str(remainder))
        x = x//2
    binary_number = "".join(s.get_stack()[::-1])
    return binary_number

print(binary(242))