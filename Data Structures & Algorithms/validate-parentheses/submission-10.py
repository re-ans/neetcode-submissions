class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s: 
            if c in mappings and stack:
                top = stack.pop()
                if mappings[c] != top:
                    return False
            else:
                stack.append(c)
        
        return not stack

