# time taken = 15 minutes

def generate_pattern(n) -> None:
    """
    Generates a pattern of n rows.
    N = 2
    # #
    # #

    N = 3
    ## ## ##
    ## ## ## 

    N = 4
    ### ### ### ###
    ### ### ### ###

    """

    for i in range(2):
        for j in range(n):
            print("#" * (n-1), end=" ")
        print("")


if __name__ == '__main__':
    n = int(input())
    generate_pattern(n)
