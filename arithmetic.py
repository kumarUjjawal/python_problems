# Task: Perform Arithmetic Operations on Two Integers Provided by the User.

def arith_operation(a:int, b:int):
    sum = a + b
    print("Sum of two numbers: ", sum)
    
    diff = a - b
    print("Difference of two numbers: ", diff)

    product = a * b
    print("Product of two numbers: ", product)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    arith_operation(a,b)