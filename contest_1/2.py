# time - 9 minutes

def make_pattern(height):
    for i in range(1, height):
        print("*"*i + " " * (height-i*2+3) + "*"*i)


if __name__ == '__main__':
    make_pattern(int(input().strip()))
