# time taken - 12 minutes

def left_right_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end=" ")
        for j in range(1, i + 1):
            print(j, end="")
        for k in list(reversed(range(1, i))):
            print(k, end="")
        print()


if __name__ == "__main__":
    rows = 5
    left_right_number_pyramid(rows)
