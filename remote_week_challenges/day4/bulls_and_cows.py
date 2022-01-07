# time taken -> 18 mins


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        cows = bulls = 0

        maps = {}

        for num in range(0, 10):
            maps[str(num)] = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cows += (maps[s] < 0) + (maps[g] > 0)
                maps[g] -= 1
                maps[s] += 1

        return f'{bulls}A{cows}B'

        # direct and limited approach with O(n) time and O(n) space

        # xAyB
        # x = Bulls (correct config)
        # y = Cows (incorrect config, but exist)

        # check if every chr in secret is in guess
        # count the check

        # exist = [char for char in secret if char in guess]  # space O(n)
        # count = len(exist)

        # # check order and decrement for every correct from cows
        # # increment for bull
        # cow = 0

        # for i in range(len(secret)):  # time O(n)
        #     if secret[i] == guess[i]:
        #         cow += 1

        # return f'{cow}A{count-cow}B'


if __name__ == "__main__":
    s = Solution()
    secret = "1807"
    guess = "7810"
    print(s.getHint(secret, guess))
