

def climbing_stairs_k_steps(n: int, k: int) -> int:
    """
    Given n stairs, how many ways can you climb up to the nth stair?
    You can climb 1 or 2 steps at a time.
    """
# a recursive solution
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # return climbing_stairs_k_steps(n - 1, k) + climbing_stairs_k_steps(n - 2, k)

    # iterative approach
    if n == 0:
        return 1
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, k+1):
            if i - j >= 0:
                dp[i] += dp[i-j]

    return dp[n]


if __name__ == "__main__":
    print(climbing_stairs_k_steps(4, 2))  # should print 5
    print(climbing_stairs_k_steps(5, 2))  # should print 8
