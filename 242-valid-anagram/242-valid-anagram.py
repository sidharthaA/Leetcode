class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = sorted(s)
        q = sorted(t)
        if p == q:
            return True
        else: 
            return False     
        # print(q)
        # for letter in t:
            