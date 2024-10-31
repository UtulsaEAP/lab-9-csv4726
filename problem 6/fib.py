def fibonacci(n):
    
    #write your code here
        # Return -1 for any negative index
    if n < 0:
        return -1
    # Handle base cases
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    # Calculate Fibonacci for other cases
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')