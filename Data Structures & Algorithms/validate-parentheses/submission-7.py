class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for c in s:

            if c in d and len(stack) != 0 and stack[-1] == d[c]:
                stack.pop()
            else:
                stack.append(c)



        return len(stack) == 0
