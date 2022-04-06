class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        left = count = 0
        right = len(people)-1
        
        people.sort()
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                left += 1

            count += 1
            right -= 1
            
        
        return count
                
        