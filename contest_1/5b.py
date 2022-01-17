#  in progress

indexAlphabet = {}

for i in range(1, 27):
    indexAlphabet[chr(i+64)] = i

# A - 1, B- 2,...  Z - 26


def get_index(column):

    split = []

    for i in column:
        if i.isalpha():
            split.append(i)

    sum = 0

    if len(split) < 2:
        return indexAlphabet.get(split[0])
    else:
        for i in split:
            sum += indexAlphabet.get(i)
        return sum


if __name__ == '__main__':
    print(get_index((input().strip())))
