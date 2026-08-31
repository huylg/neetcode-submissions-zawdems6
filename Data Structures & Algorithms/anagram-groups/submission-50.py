class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for str in strs:
            s = frozenset(Counter(str).items())
            group[s] = group.get(s, []) + [str]
        
        return list(group.values())
 

