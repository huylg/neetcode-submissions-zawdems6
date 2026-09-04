class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        result = 0

        d = defaultdict(int)

        while fast < len(s):
            while d[s[fast]] != 0:
                d[s[slow]]-=1
                slow+=1


            d[s[fast]]+=1
            fast += 1
            result = max(result, fast  - slow )
            


        result = max(result, fast  - slow )
        return result

