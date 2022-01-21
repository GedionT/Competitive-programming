# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":

    from collections import deque

    d = deque()

    for _ in range(int(input())):
        exec('d.{0}({1})'.format(*input().split()+['']))

    print(*d)


"""

n = int(input())
for i in range(n):
    choice= input().split()
    if choice[0]=="append" :
        d.append(int(choice[1]))
    elif choice[0]=="appendleft" :
        d.appendleft(int(choice[1]))
    elif choice[0]=="pop" :
        d.pop()
    elif choice[0]=="popleft" :
        d.popleft()
    
print(*d)

"""
