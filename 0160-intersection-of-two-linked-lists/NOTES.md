list1, list2 = [], []
while headA or headB:
if headA:
list1.append(headA)
headA = headA.next
if headB:
list2.append(headB)
headB = headB.next
ptr1, ptr2 = len(list1)-1, len(list2)-1
list1A = list(map(lambda x : x.val, list1))
list2A = list(map(lambda x : x.val, list2))
# print(list1)
# print(list2)
while ptr1 >= 0 or ptr2 >= 0:
# print(ptr1, ptr2)
if list1[ptr1] == list2[ptr2]:
ptr1 -= 1
ptr2 -= 1
elif len(list1) > (ptr1 + 1):
return list1[ptr1+1]
elif len(list2) > ptr2 + 1:
return list2[ptr2+1]
else:
break
return None