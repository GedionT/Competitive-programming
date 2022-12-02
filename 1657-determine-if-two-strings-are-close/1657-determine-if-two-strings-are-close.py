class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # sanity check
        if len(word1) != len(word2):
            return False

        biner_1 = [0]*26
        biner_2 = [0]*26
        
        for i in word1:
            biner_1[ord(i)-97]+=1
        for i in word2:
            biner_2[ord(i)-97]+=1
            
        for i in range(26):
            if (biner_1[i]>0 and biner_2[i]==0) or (biner_1[i]==0 and biner_2[i]>0):
                return False   
                
        biner_1.sort()
        biner_2.sort()

        if biner_1[:] == biner_2[:]:
            return True
        return False
    

        
        
            
       