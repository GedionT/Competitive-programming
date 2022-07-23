if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique = sorted(list(set(arr)))

    print(unique[-2])
