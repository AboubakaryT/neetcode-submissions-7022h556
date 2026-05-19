class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in range(len(tokens)):
            if tokens[c] != "+" and tokens[c] != "-" and tokens[c] != "/" and tokens[c] != "*" :
                stack.append(int(tokens[c]))
            elif tokens[c] == "+" or tokens[c] == "-" or tokens[c] == "/" or tokens[c] == "*":
                if tokens[c] == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                elif tokens[c] == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif tokens[c] == "*" and len(stack) >= 2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 * num1) 
                elif tokens[c] == "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1)) 
        return stack[-1]                  
