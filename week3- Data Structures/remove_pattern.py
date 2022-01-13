

class Solution:
    def remove_patter(given: str, pattern: str) -> str:

        # handle edge cases of empty strings
        if not given or not pattern:
            return given

        # handle edge cases of pattern being longer than given
        if len(pattern) > len(given):
            return given

        if pattern == given[:len(pattern)]:
            return given[len(pattern):]

        return given


if __name__ == "__main__":
    given = "AABCAAADA"
    pattern = "AA"
    print(Solution.remove_patter(given, pattern))
