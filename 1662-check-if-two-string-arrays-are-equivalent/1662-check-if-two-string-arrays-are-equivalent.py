class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = ''
        second = ''
        for word in range(1, len(word1)):
            word1[0] += word1[word]
        for word in range(1, len(word2)):
            word2[0] += word2[word]
        if word1[0] == word2[0]:
            return True
        else:
            return False
        