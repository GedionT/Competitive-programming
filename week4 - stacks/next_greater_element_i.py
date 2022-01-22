"""
# time taken: 14 min

# bruteforced

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        
        for i in nums1:
            index = nums2.index(i)
            
            if (index+1) < (len(nums2)):
                
                # add another loop in the range (index+1, len(nums2)) to find the next greater and append
                for j in range(index+1, len(nums2)-1):
                    if nums2[j+1] > nums2[j]:
                        result.append(nums2[j])
                    else:
                        result.append(-1)
            else: 
                result.append(-1)
                
        return result
        
    
"""

# time taken: 15m


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # check if it is not empty
        greater_dict = {}

        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            # when stack not empty and current number greater than top of stack
            while(stack and nums2[i] > stack[-1]):
                greater_dict[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            greater_dict[stack.pop()] = -1

        return [greater_dict[i] for i in nums1]


if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))
