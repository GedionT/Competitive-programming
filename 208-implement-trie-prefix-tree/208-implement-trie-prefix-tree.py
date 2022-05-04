# class Node:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False


# class Trie:

#     def __init__(self):
#         self.root = Node()

#     def insert(self, word: str) -> None:
#         curr = self.root
        
#         for char in word:
#             if 
        
        
        

#     def search(self, word: str) -> bool:
        

#     def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# using an array

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, word):
        current = self.root
        for char in word:
            indexOfChar = ord(char) - ord('a')
            if current.children[indexOfChar] is None:
                current.children[indexOfChar] = TrieNode()
            current = current.children[indexOfChar]
        current.isWord = True        
    
    def search(self, word, isPrefix = False): 
        current = self.root
        for char in word:
            indexOfChar = ord(char) - ord('a')
            if current.children[indexOfChar] is None:
                return False
            current = current.children[indexOfChar]
        return current.isWord or isPrefix
    
    def startsWith(self, prefix):
        return self.search(prefix, True)
    


