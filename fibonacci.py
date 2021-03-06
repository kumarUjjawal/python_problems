# fibonacci through recursion
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


# fibonacci through Memoization
# Store the results of the computational tasks when they are completed

from typing import Dict

memo: Dict[int, int] = {0:0,1:1}

def fib(n:int) -> int:
    if n not in memo:
        memo[n] = fib(n-2) + fib(n-1)
    return memo[n]

# fibonacci: Automatic Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n:int) -> int:
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

# fibonacci: iterative approach
def fibon(n:int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fibonacci(6))
    print(fib(6))
    print(fibo(6))
    print(fibon(6))
