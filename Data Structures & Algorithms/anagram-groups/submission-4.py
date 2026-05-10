class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            curr_arr = [0] * 26
            for c in s:
                curr_arr[ord(c) - ord('a')] += 1
            anagram_map[tuple(curr_arr)].append(s)
        return list(anagram_map.values())

            