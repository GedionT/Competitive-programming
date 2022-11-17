class Solution:
    def findOverlap(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
        # x overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left

        # y overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        area_of_overlap = 0
        
        # if the rectangles overlap 
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = x_overlap * y_overlap
        
        return area_of_overlap
        
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)
        
        totalArea = area_a + area_b
 
        overlap = self.findOverlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return totalArea - overlap
        