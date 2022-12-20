class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:     
        visited = set()
        
        self.dfsCount(0, rooms, visited)
        return len(visited) == len(rooms)
    
    
    def dfsCount(self, node, rooms, visited):
        if node in visited:
            return
        
        visited.add(node)
        
        for key in rooms[node]:
            self.dfsCount(key, rooms, visited)
            