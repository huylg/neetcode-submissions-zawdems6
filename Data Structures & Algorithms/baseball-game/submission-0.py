class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for operation in operations:
            if operation == "+":
                st.append(st[-1] + st[-2])
            elif operation == "C":
                st.pop()
            elif operation == "D":
                st.append(st[-1] * 2)
            else:
                st.append(int(operation))
        result = 0
        for num in st:
            result += num
        return result
