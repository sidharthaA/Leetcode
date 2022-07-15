class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        for index, i in enumerate(s):
            if i in unique:
                unique[i].append(index)
            else:
                unique[i] = [index]
        for letter in unique:
            if len(unique[letter]) < 2:
                return unique[letter][0]
        else:
            return -1