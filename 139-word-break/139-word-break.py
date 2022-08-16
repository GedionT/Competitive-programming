class TrieNode:
    
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

        
class Solution:
    
    def __init__(self) -> None:
        self.root = TrieNode()
        self.memo = {}
        
    def insert(self, word) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]     
        curr.isWord = True
        return None
            
    def startsWith(self, prefix) -> bool:
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
    def canBreak(self, s):
        root = self.root

        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].isWord:
                if s[i+1:] not in self.memo:                
                    self.memo[s[i+1:]] = self.canBreak(s[i+1:]) 
                if self.memo[s[i+1:]]:                       
                    return True                                     
            root = root.children[char]         

        return root.isWord                   
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # created a trie structure for all wordDict words
        for word in wordDict:
            self.insert(word)
        # print(self.root.children)
            
        # go through the string and check if the word can be made with break
        return self.canBreak(s)
        
        
        
            
        
        