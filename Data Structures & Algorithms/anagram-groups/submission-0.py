class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            key = tuple(sorted(Counter(str).items()))
            dict[key] = dict.get(key, []) + [str]
        return list(dict.values())
