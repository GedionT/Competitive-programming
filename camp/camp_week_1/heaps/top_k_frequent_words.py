class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # create a dictionary with word as key and frequency as value
        word_freq = {}
        for word in words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

        # create a max heap by making all values negative
        heap = []
        for key, value in word_freq.items():
            heapq.heappush(heap, (-value, key))

        # create a list to store the top k frequent words
        top_k_words = []
        for i in range(k):
            top_k_words.append(heapq.heappop(heap)[1])

        return top_k_words
