class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = {}
    
        for key,value in logs: 
            if key in hashmap: 
                hashmap[key].append(value)
            else: 
                hashmap[key] = [value]

        res = [0] * k

        for users in hashmap.keys():
            res[len(set(hashmap[users])) - 1] += 1

        return res