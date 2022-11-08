class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    res.append('%d:%02d' % (h, m))
        
        return res