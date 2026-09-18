class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curr_set = set()
        res = 0

        while r < len(s):
            while s[r] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])
            r += 1
            res = max(res, len(curr_set))
        return res
            
        