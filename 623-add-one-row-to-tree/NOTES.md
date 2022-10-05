# case when the level is 1
if d == 1:
new_root = TreeNode(v)
new_root.left = root
return new_root
​
dq = deque()
dq.append(root)
level = 1
while level != d - 1:
for _ in range(len(dq)):
curr = dq.popleft()
if curr.left:
dq.append(curr.left)
if curr.right:
dq.append(curr.right)
level += 1
​
for _ in range(len(dq)):
curr = dq.popleft()
​
left = curr.left
right = curr.right
​
new1 = TreeNode(v)
new2 = TreeNode(v)
​
curr.left = new1
new1.left = left
​
curr.right = new2
new2.right = right
​
return root