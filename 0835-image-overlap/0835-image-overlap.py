class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = [] 
        img2_ones = [] 
        
        n = len(img1)
        
        for i in range(n):
            for j in range(n): 
                if img1[i][j] == 1: 
                    img1_ones.append((i,j)) 
                if img2[i][j] == 1:
                    img2_ones.append((i,j)) 

        slide_to_count = collections.defaultdict(int) 
        ans = 0
        
        for (x1, y1) in img1_ones: 
            for (x2, y2) in img2_ones: # for every 1 in img2
                slide = (x2-x1, y2-y1) # the difference in their coordinates is how much we have to slide img1 for these two 1s to overlap!
                slide_to_count[slide] += 1 # we have an extra overlap of 1s when sliding
                ans = max(ans, slide_to_count[slide]) # update ans
        return ans