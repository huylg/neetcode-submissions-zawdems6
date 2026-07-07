class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for str in strs:
            key = hash(tuple(sorted(Counter(str).items())))
            v = s.get(key, [])
            s[key] = v + [str]
        return list(s.values())

        




