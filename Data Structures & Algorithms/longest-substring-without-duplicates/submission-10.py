class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = r = 0
        hash_map = set()
        while r < len(s):
            while s[r] in hash_map:
                hash_map.remove(s[l])
                l += 1
            hash_map.add(s[r])
            longest = max(r - l + 1, longest)
            r += 1
        return longest