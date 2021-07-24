def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0: 
        return None
    
    shortestCombination = None
    
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination =[*remainderCombination, number]
            # if combination is shorter than the shortestCombination, update the shortestCombination
            if shortestCombination is None or len(combination) < len(shortestCombination) :
                shortestCombination = combination 
    memo[targetSum] = shortestCombination
    return shortestCombination


print(bestSum(7, [5, 4, 3, 7]))
print(bestSum(1000, [5, 4, 3, 250]))