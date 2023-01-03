class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedCol = 0
        k = len(strs[0])
        
        for i in range(k):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    deletedCol += 1
                    break

        return deletedCol
                    