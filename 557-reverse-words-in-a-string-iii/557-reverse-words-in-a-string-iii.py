class Solution:
    def reverseWords(self, s: str) -> str:
        def flip_word_in_place(left_p:int, right_p: int):
            while left_p < right_p:
                s_arr[left_p], s_arr[right_p] = s_arr[right_p], s_arr[left_p]
                left_p += 1
                right_p -= 1

        left = 0
        s_arr = list(s)
        
        for i in range(len(s)):
            if s_arr[i] == " ":
                flip_word_in_place(left, i - 1)
                left = i + 1
        flip_word_in_place(left, len(s_arr)-1)
        
        return "".join(s_arr)