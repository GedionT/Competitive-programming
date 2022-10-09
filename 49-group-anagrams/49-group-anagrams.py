class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        match = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in match:
                match[sorted_string] = []

            match[sorted_string].append(string)

        return list(match.values())