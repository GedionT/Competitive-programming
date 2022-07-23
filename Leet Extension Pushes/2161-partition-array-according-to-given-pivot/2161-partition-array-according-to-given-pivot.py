class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
            9, 12, 5, 10, 14, 3, 10  ;  piv = 10
            pivArr -> 9, 5, 3, 10, 10, 12, 14

            -3, 4, 3, 2 ; piv = 2
            pivArr -> -3, 2, 4, 3
            
            
            constraint len(nums) 1 - 10^5
            nums[i]  -10^6 - 10^6
            pivot = an element of nums
        '''
        
        
        left = []
        right = []
        mid = 0
        
        for num in nums:
            
            if num > pivot:
                right.append(num)
            elif num < pivot:
                left.append(num)
            else:
                mid += 1
        

        ans = [*left, *[pivot]*mid , *right]
        print(ans)
        
        return ans
        