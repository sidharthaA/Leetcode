class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # sub = ""
        # maxSub = ""
        # l = 0
        # for i in s:
        #     sub = sub + i
        #     if sub.find(i) != sub.rfind(i):
        #         sub = sub[sub.find(i) + 1: ]   
        #     if len(sub) > l:
        #         l = len(sub)
        #         maxSub = sub
        # return(len(maxSub))
        
        start = 0
        end = 0
        maxLen = 0
        arr = []
        for i in range(len(s)):
            if s[i] not in arr:
                arr.append(s[i])
            else:
                del arr[0:arr.index(s[i]) + 1]
                arr.append(s[i])
            maxLen = max(len(arr), maxLen)
        return maxLen