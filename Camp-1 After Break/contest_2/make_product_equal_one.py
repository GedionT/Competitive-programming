n = int(input())
nums = list(map(int,input().split()))

steps = 0

zeros = []

for i in range(n):
  if nums[i] < -1:
    steps += -1 -nums[i]
    nums[i] = -1
  elif nums[i] > 1:
    steps += nums[i] - 1
    nums[i] = 1
  elif nums[i] == 0:
    zeros.append(i)
    
count = nums.count(-1)
if count %2 == 1:
    if zeros:
        nums[zeros[0]] = -1
        steps +=1
        steps += len(zeros[1:])
    else:
        steps +=2
else:
    steps += len(zeros)

        
        
            

print(steps)