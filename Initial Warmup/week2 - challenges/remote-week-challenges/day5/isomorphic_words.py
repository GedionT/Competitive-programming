# time taken -> 30 min

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hash = {}

        if len(t) != len(s):
            return False
        else:
            for i in range(len(t)):
                if t[i] in hash:
                    if hash[t[i]] != s[i]:
                        return False
                else:
                    hash[t[i]] = s[i]

            s = []
            for key, value in hash.items():
                if value in s:
                    return False
                else:
                    s.append(value)

            return True

        # not effective time complexity
        # mapST, mapTS = {}, {}

        # for i in ranage(len(s)):
        #     c1, c2 = s[i], t[i]

        #     if ((c1 in mapST and mapST[c1] != c2) or {c2 in mapTS and mapTS[c2] != c1}):
        #         return False

        #     mapST[c1] = c2
        #     mapTS[c2] = c1


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("ab", "aa"))
