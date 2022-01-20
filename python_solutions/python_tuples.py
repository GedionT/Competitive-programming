if __name__ == '__main__':
    n = int(input())
    print(hash(tuple(map(int, input().split()))))

    # python tuple is immutable, so we can't change it
    # we can't add or remove elements from a tuple
    # we can't change the order of elements in a tuple
    # we can't change the type of elements in a tuple
    # we can't delete a tuple

    #  but because a tuple is immutable, it can be hashed
    #  and we can use it as a key in a dictionary

    # hash() is built-in function in python, it returns the hash value of an object
