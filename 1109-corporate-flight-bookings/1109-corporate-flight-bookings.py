class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        line = [0] * (n+2)  
        
        for booking in bookings:
            line[booking[0]] += booking[2]
            line[booking[1]+1] -= booking[2]
            
        prefix = [0]
        
        for i in range(len(line)):
            prefix.append(prefix[-1]+line[i])
        
        
        return prefix[2:-1]

    