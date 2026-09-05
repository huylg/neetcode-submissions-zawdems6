class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        stack = []


        for i, v in enumerate(temperatures):

            while len(stack) > 0 and temperatures[stack[-1]] < v:
                j = stack.pop()
                result[j] = i - j

            stack.append(i)


        return result





