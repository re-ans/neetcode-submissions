class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            curr_anagram = [0] * 26
            for c in s:
                curr_anagram[ord(c) - ord('a')] += 1
            print(curr_anagram)
            res[tuple(curr_anagram)].append(s)
            
        
        return list(res.values())