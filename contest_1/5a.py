indexAlphabet = {}

for i in range(1, 27):
    indexAlphabet[i] = chr(i+64)


def get_index(column) -> str:

    if column <= 26:
        return indexAlphabet.get(column)
    elif column > 26:
        rounded = column % 26
        return "A" + indexAlphabet.get(rounded)


if __name__ == '__main__':
    print(get_index(int(input().strip())))
