

class Solution:

    def swap_case(input_string):

        swapped_string = [char.lower() if char.isupper() else char.upper()
                          for char in input_string]

        print(swapped_string)


if __name__ == "__main__":

    sol = Solution()

    sol.swap_case("TheHiddEnSamI")
