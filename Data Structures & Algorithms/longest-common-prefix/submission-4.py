class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i, c in enumerate(strs[0]):
            temp = True
            for s in strs:
                temp &= len(s) > i and s[i] == c
            if temp:
                result += c
            else:
                return result

        return result
