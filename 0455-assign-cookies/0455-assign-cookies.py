class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0

        while i < len(g) and j < len(s):
            while g[i] > s[j]:
                if j < len(s) - 1:
                    j += 1
                else:
                    return count
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
        return count