class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')' : '(', ']' : '[', '}' : '{'}
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i not in dict:
                stack.append(i)
            elif stack == [] or dict[i] != stack.pop(-1):
                return False
        return stack == []