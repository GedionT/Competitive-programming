class Solution:
    def findKey(self, log):
        _id, data = log.split(" ", maxsplit=1)
        
        if data[0].isalpha():
            return (0, data, _id) 
        else:
            return (1, )
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        return sorted(logs, key=self.findKey)