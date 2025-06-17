class Solution:
    def scoreOfString(self, s: str) -> int:
        total, prev = 0, s[0]
        for curr in s[1:]:
            total += abs(ord(prev) - ord(curr))
            prev = curr
        return total