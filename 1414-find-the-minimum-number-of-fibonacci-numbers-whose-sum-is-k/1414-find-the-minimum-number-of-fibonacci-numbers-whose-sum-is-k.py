class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        curr_element = 1
        sequence = [1]
        while curr_element <= k:
            sequence.append(curr_element)
            curr_element = sequence[-1] + sequence[-2]

        # make my greedy choice
        # if I can use a current element, I'd use it, if not, I would just jump to next element
        number_of_fibb = 0
        while sequence and k > 0:
            last_element = sequence.pop()
            if k - last_element >= 0:
                number_of_fibb += (k // last_element)
                k -= last_element

        return number_of_fibb