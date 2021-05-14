# given an array corresponding to the price of stock on a given day
# find the max amount of profit that can be made by buying and selling

array = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Brute Force Approach
# Time Complexity: O(N**2)
# Space Complexity: O(1)


def bruteforce(array):
    max_profit = 0
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[j] - array[i] > max_profit:
                max_profit = array[j] - array[i]

    return max_profit


print(bruteforce(array))

# Minimum element approach
# Time Complexity: O(N)
# Space Complexity: O(1)


def approach2(array):
    min_till_now = array[0]
    max_difference = 0
    for ele in array:
        min_till_now = min(min_till_now, ele)
        difference = ele - min_till_now
        max_difference = max(max_difference, difference)

    return max_difference


print(approach2(array))
