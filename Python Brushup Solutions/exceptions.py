# Enter your code here. Read input from STDIN. Print output to STDOUT


for _ in range(int(input())):

    try:
        a, b = map(int, input().strip().split())
        print(a//b)
    except ZeroDivisionError as err:
        print(f"Error Code: {err}")
    except ValueError as err:
        print(f"Error Code: {err}")
