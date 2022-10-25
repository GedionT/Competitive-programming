class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False


        # edge case
        if s == goal:
            s_count = Counter(s)

            for ch in s_count:
                if s_count[ch] >= 2:
                    return True
            return False

        s = list(s)

        # generalized two pointer solution
        not_similar = []
        ptr = 0

        while ptr < len(s):
            if s[ptr] != goal[ptr]:
                not_similar.append((s[ptr], goal[ptr]))
                                   
            if len(not_similar) > 2:
                return False 
            
            ptr += 1

        print(not_similar)
        return len(not_similar) == 2 and not_similar[0] == not_similar[1][::-1]