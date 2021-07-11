# Problem statement in one note

def howSum(targetSum, numbers):
    #base cases
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    #branching logic
    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            return [*remainderResult, number]
    
    return None

def howSum_opt(targetSum, numbers, memo = {}):
    #returning memo values
    if targetSum in memo:
        return memo[targetSum]
    
    #base cases
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    #branching logic
    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSum_opt(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetSum] =  [*remainderResult, number]
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(65, [8, 7]))