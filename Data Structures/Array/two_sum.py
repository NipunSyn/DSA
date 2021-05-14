# given a sorted array of int
# return the two numbers such that they add up to the specific target
# problem has exactly one solution
# can't use the same element twice
# already solved using dictionary. Now array

array = [-2, 1, 2, 4, 7, 11]
target = 13

# Naive approach: Brute force
# Time Complexity: O(N**2)
# Space Complexity: O(1)


def brute_force(array, target):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return i, j
    return False


print(brute_force(array, target))

# Dictionary Approach
# Time Complexity: O(N)
# Space Complexity: O(N)


def hashtable(array, target):
    hashtable = dict()
    for index, value in enumerate(array):
        pair = target-value
        if pair in hashtable:
            return hashtable[pair], index
        else:
            hashtable[value] = index
    return False


print(hashtable(array, target))

# Two pointer approach- makes use of sorted array
# Time Complexity: O(N)
# Space Complexity: O(1)


def two_pointer(array, target):
    i = 0
    j = len(array) - 1

    while i <= j:
        if array[i] + array[j] == target:
            return i, j
        elif array[i] + array[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(two_pointer(array, target))
