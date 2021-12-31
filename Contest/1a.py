# time 9

def make_stars(height) -> None:
    """
    Prints an equilateral triangle of height=height.
    """
    for i in range(height):
        if i == 1:
            print(' ' * (height-i-1) + '*')
        if i % 2 != 0:
            print(' ' * (height-i-2) + "*" * (i+2))


if __name__ == '__main__':
    make_stars(6)
# int(input().strip())
