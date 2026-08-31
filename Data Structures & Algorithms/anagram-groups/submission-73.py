class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            so = "".join(sorted(s))
            group[so] = group.get(so, [])
            group[so].append(s)


        return list(group.values())



 

