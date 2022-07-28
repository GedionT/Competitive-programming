class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# alt 1: straight forward O(nlogn)      
#         if sorted(s) == sorted(t):
#             return True
        
#         O(n) space and O(n) complexity
        dictionary = collections.defaultdict(int)
        
        for c in s: dictionary[c] += 1
        for c in t: dictionary[c] -= 1
            
        return all(c == 0 for c in dictionary.values())