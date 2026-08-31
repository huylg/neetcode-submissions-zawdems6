class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            so = "".join(sorted(s))

            if so in group:
                group[so].append(s)
            else:
                group[so] = [s]


        return list(group.values())




 

