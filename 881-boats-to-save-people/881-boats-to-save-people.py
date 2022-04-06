class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        left = count = 0
        right = len(people)-1
        
        people.sort()
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                count += 1
                
                left += 1
                right -= 1
            
            else:
                count += 1
                right -= 1
        
        return count
                
        