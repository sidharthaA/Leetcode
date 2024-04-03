class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        rel = {}
        s_list = s.split(" ")
        if len(set(s_list)) != len(set(pattern)) or len(s_list) != len(pattern):
            return False
        while i < len(pattern):
            if pattern[i] not in rel:
                rel[pattern[i]] = s_list[i]
            else:
                if rel[pattern[i]] != s_list[i]:
                    return False
            i += 1
        return True