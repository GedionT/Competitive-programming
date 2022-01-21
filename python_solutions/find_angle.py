import math

AB = int(input())
BC = int(input())

AC = math.hypot(AB, BC)     # c= sqrt(a^2 + b^2)

res = round(math.degrees(math.acos(BC/AC)))  # acos or btan
degree = chr(176)

print(f'{res}{degree}')
