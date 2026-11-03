class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        res = 1
        char_set = set()
        char_set.add(s[l])

        for r in range(1, len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            res = max(res, len(char_set))
        
        return res