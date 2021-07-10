# problem statement in notes

# Naive approach, slow
def gridTraveller(m, n):
    
    #writing the base cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    #rest of the cases
    return gridTraveller(m-1, n) + gridTraveller(m, n-1)

# Optimized approach, way more efficient

def gridTraveller_opt(m, n, memo = {}):
    # check if the arguements are in the memo
    
    key = f"{m}, {n}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    memo[key] = gridTraveller_opt(m - 1, n, memo) + gridTraveller_opt(m, n - 1, memo)
    
    return memo[key]



print(gridTraveller(2, 2))
print(gridTraveller(3, 3))
print(gridTraveller_opt(25, 25))