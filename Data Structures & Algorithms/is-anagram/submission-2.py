class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = [0] * 128;

        for char in s:
            seen[ord(char)] += 1
        
        for char in t:
            seen[ord(char)] -= 1

        return not any(seen)
        