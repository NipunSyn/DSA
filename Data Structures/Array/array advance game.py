#Given an array of integers, with each integer representing the maximum number of steps that we can take to the right. Find out if we can reach the last element of the array.

#Greedy approach will not work here always

def advance(array):
    furthest_reached = 0
    last_index = len(array) - 1
    i = 0
    
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, array[i]+i)
        i += 1
    return furthest_reached >= last_index


array1 = [3, 3, 1, 0, 2, 0]
print(advance(array1))
array2 = [3, 2, 0 ,0 ,3, 1, 1]
print(advance(array2))