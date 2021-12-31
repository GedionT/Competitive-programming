

def generate_diamond_pattern_numbers(rows):

    #  generate upper half
    for i in range(1, rows + 1):
        print(" " * (rows - i), end=" ")
        for j in range(1, i + 1):
            print(j, end="")
        for k in list(reversed(range(1, i))):
            print(k, end="")
        print()
    # generate lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end=" ")
        for j in range(1, i + 1):
            print(j, end="")
        for k in list(reversed(range(1, i))):
            print(k, end="")
        print()


if __name__ == "__main__":
    rows = 5
    generate_diamond_pattern_numbers(rows)
