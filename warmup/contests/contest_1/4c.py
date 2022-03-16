
def generate_hash(rows):

    for i in range(1, 26):
        if i % 2 == 0:
            print(" " * 2, end="")
        else:
            print("#" * 2, end="")

        if i % rows == 0:
            print()


if __name__ == "__main__":
    rows = 5
    generate_hash(rows)
