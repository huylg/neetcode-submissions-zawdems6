class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+',
            '-',
            '*',
            '/',
        }



        stack = []

        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()

                if token == '+': 
                    stack.append(second + first)
                elif token == '-': 
                    stack.append(first - second)
                elif token == '*': 
                    stack.append(second * first)
                else:
                    stack.append(int(first / second))

            else:
                stack.append(int(token))



        return stack[0]

