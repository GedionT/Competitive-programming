"""
 S contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

"""


n = input()
l = []
u = []
o = []
e = []
for i in n:
    if i.islower():
        l.append(i)
    elif i.isupper():
        u.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            e.append(i)
        elif int(i) % 2 != 0:
            o.append(i)
a = sorted(l)+sorted(u)+sorted(o)+sorted(e)
for i in a:
    print(i, end="")
