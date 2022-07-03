class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []
        for i in s:
            if i.isalnum():
                p.append(i)
        start = 0
        end = len(p) - 1
        while start < end:
            if p[start].lower() != p[end].lower():
                return False            
            start = start + 1
            end = end - 1
        return True
        