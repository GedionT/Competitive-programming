class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, words):
        curr = self.root
        
        for char in words:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True
            
    def startsWith(self, word):
        curr = self.root
        
        s = ""
        for char in word:
            if curr.isEnd:
                return s
            if char not in curr.children:
                return word
    
            curr = curr.children[char]
            s += char
            
        return word
            
            
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        for words in dictionary:
            self.insert(words)
        
        res = ""
        for word in sentence.split(" "):
            res += self.startsWith(word)
            res += " "
            
        return res.strip()
            