class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # fleet = non-empty set driving at the same position and same speed
        #       = single car is also considered a fleet
        
        
        # target = distance of destination
        
        # create an array of position and speed pair
        pair= [[p, s] for p,s in zip(position, speed)]
        
        stack = []
        
        for p, s in reversed(sorted(pair)): 
            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # because we are in reversed order, collision don't need be checked for each one left and there is no while loop
                stack.pop()
        
        return len(stack)
            
            
        
        