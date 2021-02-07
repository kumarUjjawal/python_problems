# Task: Given an integer n, perporm some conditional operations.
import sys
def conditional_actions(n:int):
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    conditional_actions(n)