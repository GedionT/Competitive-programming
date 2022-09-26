
def recur(lst, i):

    if i < len(lst):
        lst[i] = lst[i] + 1
        recur(lst, i+1)

    return lst


print(recur([1, 2, 3, 4, 5], 0))

- list passed by reference in recursion while 
- normal variables passed by value (copy)