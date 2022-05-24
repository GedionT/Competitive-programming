
def climb_stairs(n: int) -> int:
    """Problem: Climbing Stairs
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?

    Framework for solving DP Problems:
        1. Define the objective function
            f(i) is the number of distinct ways to reach the i-th stair
        2. Identify base cases - also can be edge cases (Be on the lookout)
            f(0) = 1
            f(1) = 1
        3. Write down a recurrence relation for the optimized objective function
            f(n) = f(n-1) + f(n-2)
        4. What's the order of execution?
            Bottom-up - because we are always relying on the values of the two previous sub problems
        5. Where to look for the answer?
            f(n)


        Analysis: 
            Time Complexity: O(n)
            Space Complexity: O(n)
    """
    # recursively calculate the number of ways to reach the n-th stair
    # if n == 0:
    #     return 1
    # elif n == 1:
    #     return 1
    # else:
    #     # f(n) = f(n-1) + f(n-2)
    #     return climb_stairs(n-1) + climb_stairs(n-2)

    # iteratively
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize the array
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    # Fill in the rest of the array
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


if __name__ == "__main__":

    print(climb_stairs(3))
    print(climb_stairs(5))
