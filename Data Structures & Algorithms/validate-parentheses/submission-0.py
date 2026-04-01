class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        
        for c in s:
            if c in {'[','{','('}:
                st.append(c)
            elif len(st) == 0 or st.pop() != d[c]:
                return False
                

        return not st
