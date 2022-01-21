

class Solution:
    def remove_patter(given: str, pattern: str) -> str:

        # handle edge cases of empty strings
        if not given or not pattern:
            return given

        # handle edge cases of pattern being longer than given
        if len(pattern) > len(given):
            return given

        given = list(given)
        pattern = list(pattern)

        stack = []
        pattern_len = len(pattern)

        for i in range(len(given)):
            if given[i] != pattern[-1]:
                stack.append(given[i])
            elif given[i] == pattern[-1]:
                if stack[::-pattern_len] == pattern:
                    stack.pop[::-pattern_len]
            else:
                pass


if __name__ == "__main__":
    given = "AABAAADA"
    pattern = "AB"
    print(Solution.remove_patter(given, pattern))
