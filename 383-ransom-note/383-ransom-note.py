class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        
        for i in r_count:
            if m_count[i] < r_count[i] or i not in m_count:
                return False
        
        return True