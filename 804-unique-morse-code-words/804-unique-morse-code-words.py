class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        seen = set()
        
        for word in words:
            morsed = ""
            for char in word:
                morsed += morse[ord(char)-97]
            seen.add(morsed)
        
        return len(seen)
                
                