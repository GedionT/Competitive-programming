
class Tree:
    def __init__(self, root=0, left=None, right=None):
        self.root = root
        self.right = right
        self.left = left


def dfs(root):

    # base case
    if not root:
        return 0

    # recurrence relationship
    return sum(dfs(root.left), dfs(root.right))


if __name__ == "__main__":

    t1 = Tree(4, 5, 5)

    print(dfs(t1.root))
