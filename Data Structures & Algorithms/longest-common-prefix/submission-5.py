class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
            result = ""

            for i, c in enumerate(strs[0]):
                for s in strs:
                    if len(s) <= i or s[i] != c:
                        return result

                result += c

            return result
