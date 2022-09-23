class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse_words_inplace(left_ptr: int, right_ptr: int) -> None:
            
            while left_ptr < right_ptr:
                s_list[left_ptr], s_list[right_ptr] = s_list[right_ptr], s_list[left_ptr]
                left_ptr += 1
                right_ptr -= 1
            
        
        left = 0
        s_list = list(s)
        
        for i in range(len(s)):
            if s_list[i] == ' ':
                reverse_words_inplace(left, i-1)
                left = i + 1
        
        reverse_words_inplace(left, len(s)-1)
        
        return ''.join(s_list)