class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = [0] * 128;
        seen2 = [0] * 128

        for char in s:
            seen1[self.hashFunc(char)] += 1
        
        for char in t:
            seen2[self.hashFunc(char)] += 1

        return seen1 == seen2
        
        


    def hashFunc(self, c) -> int:
        return ord(c)