class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_freq = 0
        char_count = {}

        for r in range(len(s)):
            r_char = s[r]
            char_count[r_char] = char_count.get(r_char, 0) + 1
            max_freq = max(max_freq, char_count[r_char])

            if (r - l + 1) - max_freq > k:
                l_char = s[l]
                char_count[l_char] -=  1
                l += 1
            
            res = max(res, r - l + 1)
        return res