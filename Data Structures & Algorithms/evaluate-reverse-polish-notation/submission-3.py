class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack of 2 numbers
        # first pop the first 2
        # then at an operator, perform the operation on both
        # and pop

        stack = []
        res = 0
        
        for c in tokens:
            if c not in ('+', '-', '*', '/'):
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))

        return stack[0]

