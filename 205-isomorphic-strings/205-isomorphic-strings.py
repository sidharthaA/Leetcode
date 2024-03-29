class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        testDict1 = {}
        testDict2 = {}
        count = 0
        for index, character in enumerate(s):
            if character in testDict1:
                testDict1[character].append(index)
            else:
                testDict1[character] = [index]
                count += 1
        for index, character in enumerate(t):
            if character in testDict2:
                testDict2[character].append(index)
            else:
                testDict2[character] = [index]
                count -= 1
        if count == 0:
            for val in testDict2.values():
                if val not in testDict1.values():
                    return False
        else:
            return False
        return True