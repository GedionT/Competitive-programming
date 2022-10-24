class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s = list(s)
        goal = list(goal)

        # edge case
        if s == goal:
            s_count = Counter(s)

            for ch in s_count:
                if s_count[ch] >= 2:
                    return True
            return False


        # generalized two pointer solution
        not_similar_s = []
        not_similar_goal = []

        ptr = 0

        while ptr < len(s):
            if s[ptr] != goal[ptr]:
                not_similar_s.append(s[ptr])
                not_similar_goal.append(goal[ptr])

            ptr += 1

        if len(not_similar_s) > 2:
            return False

        if set(not_similar_s) == set(not_similar_goal):
            return True

        return False