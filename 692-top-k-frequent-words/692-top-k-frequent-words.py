# using a heap
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         # create a dictionary with word as key and frequency as value
#         word_freq = {}
#         for word in words:
#             if word not in word_freq:
#                 word_freq[word] = 1
#             else:
#                 word_freq[word] += 1
        
#         # create a max heap by making all values negative
#         heap = []
#         for key, value in word_freq.items():
#             heapq.heappush(heap, (-value, key))
        
#         # create a list to store the top k frequent words
#         top_k_words = []
#         for i in range(k):
#             top_k_words.append(heapq.heappop(heap)[1])
        
#         return top_k_words
    
    
# using trie

class Node:
    def __init__(self):
        self.children = {}
        self.freq = 1

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        root = Node()
        for word in words:
            if word in root.children:
                root.children[word].freq += 1
            else:
                root.children[word] = Node()
                
        words = []
        
        for word in root.children:
            words.append([-1 * root.children[word].freq, word])
        
        words.sort()
        
        for i in range(len(words)):
            words[i] = words[i][1]
        return words[:k]
        
        
        
        
        
        
        
    