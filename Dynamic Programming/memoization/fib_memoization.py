 #recursive method
 #would fail for large numbers
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

#memoized method
#using a dictionary to store the values. keys will be the arguement, and value will be the return value of the function

def fib_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <=2:
        return 1;
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


print(fib_memo(100))