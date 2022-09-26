
# def is_path_possible(start, finish, front, back) -> str:

    

if __name__ == "__main__":
    test = int(input())

    for i in range(test):
        _ = input()

        n_station, queries = map(int, input().split())

        stations = input().split()

        front = {}
        back = {}
        for i, x in enumerate(stations):
            if x not in front:
                front[x]=i
            back[x]=i

        for _ in range(queries):
            start, finish = map(int, input().split())

            if start in front and finish in back and front[start]<back[finish]:
                print("YES")
            else:
                print("NO")




"""
for _ in range(int(input())):
    input()
    n, k = map(int,input().split())
    stations =  input().split()
    front = {}
    back = {}
    for i, x in enumerate(stations):
        if x not in front:
            front[x]=i
        back[x]=i
    for i in range(k):
        a, b = input().split()
        if a in front and b in back and front[a]<back[b]:
            print("YES")
        else:
            print("NO")
            
"""