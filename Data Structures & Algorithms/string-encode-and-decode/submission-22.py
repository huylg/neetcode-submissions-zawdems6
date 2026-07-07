class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += '*' + str(len(s)) + '*' + s
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s):
            i += 1
            l = 0
            while s[i] != '*':
                l = l*10 + int(s[i])
                i += 1
            i += 1
            strs.append(s[i : i + l])
            i += l

        return strs

