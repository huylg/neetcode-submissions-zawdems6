from operator import add, truediv, sub, mul

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
          
        dict = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
        }
        
        st = []
        
        for token in tokens:
            if token not in dict.keys():
                st.append(int(token))
            else:
                a = st.pop()
                b = st.pop()
                val = int(dict[token](b,a))
                st.append(val)
        
        return st[-1]
