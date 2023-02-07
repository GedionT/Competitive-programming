class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        posX, posY = 0, 1
        x, y = 0, 0
        
        for direction in instructions:
            if direction == "G":
                x += posX
                y += posY
                
            elif direction == "L": # vector translation
                posX, posY = -1*posY, posX
                
            else:
                posX, posY = posY, -1*posX
                
        
        return (x, y) == (0, 0) or (posX, posY) != (0, 1) # if no direction change in the end 