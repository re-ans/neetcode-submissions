class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res