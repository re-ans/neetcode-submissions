class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []

        mappings = {"]" : "[", "}" : "{", ")" : "("}
        
        for c in s:
            if c in mappings and stack:
                if stack.pop() != mappings[c]:
                    return False
            else:
                stack.append(c)
            print(stack)

        return not stack
