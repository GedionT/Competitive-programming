# time 5 min

def make_stars(height) -> None:
    """
    Prints a right angle triangle of height= height.
    """
    for i in range(height):
        print("*" * (i + 1))


if __name__ == '__main__':
    make_stars(int(input().strip()))
