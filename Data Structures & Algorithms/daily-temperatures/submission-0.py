class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0]*len(temperatures)
        
        for i,t in enumerate(temperatures):
            
            while st and st[-1][1] < t:
                p_i, _ = st.pop()
                result[p_i] = i - p_i
            

            st.append((i,t))
            
        return result 
