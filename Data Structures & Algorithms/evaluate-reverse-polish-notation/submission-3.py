class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}

        for c in tokens:
            if c in operators:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    stack.append(a+b)
                elif c == '-':
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))
            else:
                stack.append(int(c))
        
        return stack[0]