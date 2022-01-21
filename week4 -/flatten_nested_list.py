# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
    """


# push all the data into a stack .. last to first
# pop it as long as it doesn't have a nested value in a reverse order

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        stack = nestedList[::-1]
        self.result, self.index = [], 0

        while stack:
            nestedInt = stack.pop()

            if nestedInt.isInteger():
                self.result.append(nestedInt.getInteger())
            else:
                for innerVal in nestedInt.getList()[::-1]:
                    stack.append(innerVal)

    def next(self) -> int:
        temp = self.index
        self.index += 1
        return self.result[temp]

    def hasNext(self) -> bool:
        return self.index < len(self.result)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
