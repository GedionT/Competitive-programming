cube = lambda x: pow(x, 3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    # Recursion takes a lot of memory. Instead, use dynamic programming with generator:def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))