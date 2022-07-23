K, lst = int(input()), list(map(int, input().split()))

any_palindromes = any([str(l) == str(l)[::-1] for l in lst])
all_positives = all(l > 0 for l in lst)

print(all([any_palindromes, all_positives]))

"""
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

all()
This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

"""
