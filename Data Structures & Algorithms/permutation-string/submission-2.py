class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # since there are only 26 letters, use an array of 26 items
        s1_count = [0] * 26
        window_count = [0] * 26

        # fill the freq array for s1 to match
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # immediately if they both are teh same
        if s1_count == window_count:
            return True
        
        # since we know they didn't match, start from len(s1)
        for r in range(len(s1), len(s2)):
            # new character
            window_count[ord(s2[r]) - ord('a')] += 1
            leaving_char = r - len(s1)
            window_count[ord(s2[leaving_char]) - ord('a')] -= 1
            
            # check after each iteration
            if window_count == s1_count:
                return True
        
        return False
            
