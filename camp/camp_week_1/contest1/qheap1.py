import heapq

queries = int(input())

arr = []
heapq.heapify(arr)

for i in range(queries):
    v = list(map(int, input().split()))
    
    if len(v) < 2:
        print(arr[0])
    
    if v[0] == 1:
        heapq.heappush(arr, v[1])
    
    elif v[0] == 2:
        #  remove v[1] from heap
        #  assume v[1] always in heap
        arr2 = arr.copy()
        index = -1
        
        while arr2:
            tmp = heapq.heappop(arr2)
            if tmp != v[1]:
                index += 1
        #    swap v[1] with last element in heap


        
        
     


    
    else:
        pass
        
        