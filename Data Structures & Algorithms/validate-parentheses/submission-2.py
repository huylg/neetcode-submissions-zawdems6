class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        
        for c in s:
            if c in d.values():
                st.append(c)
            elif not st or st.pop() != d[c]:
                return False
                

        return not st
