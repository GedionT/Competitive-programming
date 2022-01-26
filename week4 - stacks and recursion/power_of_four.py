from sympy import Q


class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True

        elif n == 0 or n % 4 != 0:
            return False

        else:
            return self.isPowerOfFour(n//4)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour(27))
    print(sol.isPowerOfFour(0))
    print(sol.isPowerOfFour(4))
