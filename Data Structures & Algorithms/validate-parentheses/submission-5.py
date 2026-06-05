class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')' : '(',
                    '}' : '{',
                    ']' : '['}
        stack = []

        for c in s:
            if c in hash_map.values():
                stack.append(c)
            elif c in hash_map:
                if not stack or stack[-1] != hash_map[c]:
                    return False
                stack.pop()
        return len(stack) == 0

