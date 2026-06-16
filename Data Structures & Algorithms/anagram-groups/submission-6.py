class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            curr_anagram = "".join(sorted(word))
            anagram_map[curr_anagram].append(word)
        
        return list(anagram_map.values())

        
