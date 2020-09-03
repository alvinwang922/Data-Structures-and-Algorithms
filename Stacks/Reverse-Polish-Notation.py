"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would 
always evaluate to a result and there won't be any divide by zero operation.
"""


class Solution:
    def evalRPN(self, tokens: List[str]):
        stack = []
        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "/":
                right = stack.pop()
                left = stack.pop()
                isInt = left % right == 0
                left //= right
                if left < 0 and not isInt:
                    left += 1
                stack.append(left)
            else:
                stack.append(int(item))
        return stack.pop()


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print("The values above should be 9, 6, and 22.")
