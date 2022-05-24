s = input().strip()[::-1]  # reverse on input
t = input().strip()[::-1]

count = idx = 0
min_len = min(len(s), len(t))


while idx < min_len:
    if s[idx] == t[idx]:
        idx += 1
    else:
        break

moves = len(s) + len(t) - 2 * idx
print(moves)

# TLE when s and t are very long
# while s != t:
#     if len(s) > len(t):
#         s.pop(0)
#     else:
#         t.pop(0)
#     count += 1
