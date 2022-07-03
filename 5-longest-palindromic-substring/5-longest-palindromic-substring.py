class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l, r):
            global resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        global resLen, res
        resLen = 0
        res = ""
        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i + 1)
        return res   