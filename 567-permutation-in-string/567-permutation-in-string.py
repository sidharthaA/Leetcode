class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s1) > len(s2): return False
        for char in s1:
            if char not in d1: d1[char] = 1
            else: d1[char] += 1
        # print("d1:", d1)
        for char in s2[0:len(s1)]:
            if char not in d2: d2[char] = 1
            else: d2[char] += 1
        if d1 == d2:
            return True
        i, j = 0, len(s1) - 1
        
        while j < len(s2) - 1:
            
            if d2[s2[i]] > 1: 
                d2[s2[i]] -= 1
            else: 
                del d2[s2[i]]
            i += 1
            j += 1
            if s2[j] not in d2:
                d2[s2[j]] = 1
            else: 
                d2[s2[j]] += 1
            # print(i, j, "\n", d2)
            if d1 == d2:
                return True   
        return False
        