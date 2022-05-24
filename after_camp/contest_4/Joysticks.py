# given the battery amount of two joysticks
# return the max minutes that you can play
# 2% discharge per minute if not charging and 1% charge per minute if charging
# you can charge one at a time

a1, a2 = map(int, input().split())

count = 0




while a1 > 0 and a2 > 0:

    if a1 == 1 and a2 == 1:
        break

    if a1 > a2:
        a1 -= 2
        a2 += 1
    else:
        a1 += 1
        a2 -= 2

    count += 1


print(count)
