for _ in range(int(input())):
    n = int(input())

    a = [int(x) for x in input().split()]

    ans =0

    for i in range(n-1):
        ans+=a[i]
    if ans==0:
        print(0)
    else:
        start=0
        for i in range(n-1):
            if a[i]!=0:
                start=i
                break
        for i in range(start,n-1):
            if a[i]==0:
                ans+=1
        print(ans)