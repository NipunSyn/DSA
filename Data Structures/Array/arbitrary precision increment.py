#Given an array of non-negative digits that represent a  decimal integer. Add one to that number

#eg, given array: [1, 4, 9] will represent 149
#adding 1 to the number, we get 150, represented as [1, 5, 0]

#standard school approach of propagating the carry

def increment(array):
    our_sum = array[-1] + 1
    if our_sum == 10 and len(array) == 1:
        return [1, 0]
    
    if our_sum < 10:
        array[-1] = array[-1] + 1
        return array
    
    array[-1] = 0
    carry = 1    
    for i in range(len(array)-2, -1, -1):
        if array[i] + carry < 10:
            array[i] = array[i] + carry
            break
        else:
            if i == 0:
                new_array = [0 for _ in range(len(array) + 1)]
                new_array[0] = 1
                return new_array
            array[i] = 0
            carry = 1
            
    return array

array1 = [9]
print(increment(array1))
array2 = [9, 9, 9, 9, 9]
print(increment(array2))
            