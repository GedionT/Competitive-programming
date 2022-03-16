

def max_solved(n: int, k: int) -> int:
    '''
    Accepts n - the number of problems
    Accepts k - the time it takes to reach destination

    each problem duration 5*i

    '''
    max_mins = 240 - k
    solved_mins = 0

    for i in range(1, n + 1):

        solved_mins += (5*i)

        if solved_mins == max_mins:
            return i
        elif solved_mins >= max_mins:
            return i - 1
        else:
            continue

    return n


if __name__ == "__main__":

    print(max_solved(int(input()), int(input())))
