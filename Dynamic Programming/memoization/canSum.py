# problem statement in one note
import sys
sys.setrecursionlimit(10**6)

def canSum(targetSum, numbers):
    # base cases
    if targetSum == 0:
        return True
    
    if targetSum <0:
        return False
    
    # other cases
    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder, numbers) == True:
            return True
    
    return False


def canSum_opt(targetSum, numbers, memo = {}):
    # returning memo values
    if targetSum in memo:
        return memo[targetSum]
    
    # other base cases
    if targetSum == 0:
        return True
    
    if targetSum <0:
        return False
    
    # other cases
    for number in numbers:
        remainder = targetSum - number
        if canSum_opt(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

print(canSum(7, [5, 3]))
print(canSum(7, [4, 3]))
print(canSum_opt(701, [3, 10, 14]))