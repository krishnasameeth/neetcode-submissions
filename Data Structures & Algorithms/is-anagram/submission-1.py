class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq_s, freq_t = {}, {}

        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        for char, freq in freq_s.items():
            if freq != freq_t.get(char, 0):
                return False
        return True