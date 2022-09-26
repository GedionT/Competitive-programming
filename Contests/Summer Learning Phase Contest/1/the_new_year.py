

def find_short_distance(x: int, y: int, z: int) -> int:

    # sort the three numbers
    x, y, z = sorted([x, y, z])
    return (z - y) + (y - x)


if __name__ == "__main__":

    x, y, z = map(int, input().split())

    print(find_short_distance(x, y, z))
