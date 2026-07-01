class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                para = stack.pop()
                if (para == '(' and s[i] == ")" or 
                   para == '{' and s[i] == "}" or 
                   para == '[' and s[i] == "]"):
                   continue
                else:
                    return False
        return len(stack) == 0
