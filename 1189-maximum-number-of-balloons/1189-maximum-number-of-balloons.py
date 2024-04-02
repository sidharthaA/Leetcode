class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {}
        if 'b' not in text or 'a' not in text or 'l' not in text or 'o' not in text or 'n' not in text:
            return 0
        for i in text:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        factor = min(map['b'] * 2, map['a'] * 2, map['l'], map['o'], map['n'] * 2)
        return factor // 2