

def increase_and_copy():
    """
    find minimum number of moves required to obtain the array 
    with sum at least n

    moves:
    1. increase the last element by 1 - choose some i from 1 to current length of a
    2. append copy of some single element of a to the end of array 0 choose some i from 1 to current length of a

    """
    

    


if __name__ == "__main__":

    tests = int(input())

    ans = []

    for _ in range(tests):
        n = int(input())
        ans.append(increase_and_copy(n))
    
    for i in ans:
        print(i)
