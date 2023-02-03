class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # replace punctuations with spaces, and put all letter in lower case
        normalized_str = ''.join([ char.lower() if char.isalnum() else ' ' for char in paragraph])
        
        # split string to words
        words = normalized_str.split()
        
        # count the frequency of all words and make set
        count = Counter(words)
        banned = set(banned)
        
        ans = ""
        length = 0
        
        for key in count:
            if key not in banned:
                if count[key] > length:
                    length = count[key]
                    ans = key
        
        return ans
        
        
        