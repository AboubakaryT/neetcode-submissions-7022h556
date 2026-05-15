class Solution:
    def isValid(self, s: str) -> bool:
        # ( = ), [ = ], { = }
        contain = "({["
        stack = []
        """
        if the stack is empty or the open braket does not match the closing braket
        return false
       """
        #([{}])
        for i in s:
            if i in contain:
                stack.append(i)
            if not stack:
                return False
            else:
                if i == ")" and stack.pop()!= "(":
                    return False
                elif i == "]" and stack.pop()!= "[":
                    return False
                elif i == "}" and stack.pop()!= "{":
                    return False          

        return not stack