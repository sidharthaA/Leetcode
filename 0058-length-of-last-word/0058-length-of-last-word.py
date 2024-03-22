class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strip = s.strip()
        words = strip.split()
        return len(words[-1])