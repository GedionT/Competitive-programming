
def findEmotion(n: int) -> str:
    """
    For example if n=1, then his feeling is "I hate it" or 
    if n=2 it's "I hate that I love it", and 
    if n=3 it's "I hate that I love that I hate it" and so on.
    if n=4 "I hate that I love that I hate that I love it"
    if n=5 "I hate that I love that I hate that I love that I hate it"
    """

    if n == 1:
        return "I hate it"

    if n % 2 == 0:
        t = n // 2

        if t == 1:
            return "I hate that I love it"
        else:
            return "I hate that I love that " * (t-1) + "I hate that I love it"

    else:
        t = n // 2
        return "I hate that I love that " * t + "I hate it"


if __name__ == "__main__":

    n = int(input())

    print(findEmotion(n))
