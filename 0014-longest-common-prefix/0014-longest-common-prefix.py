class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = len(min(strs, key = len))
        # print(chars)
        ans = ""
        for char in range(1, chars + 1):
            # print("char: ", char)
            ans = strs[0][:char]
            # print("ans: ", ans)
            for s in strs:
                if s[:char] != ans:
                    # print("s[:char]: ", s[:char])
                    # print("ans[:-1]: ", ans[:-1])
                    return ans[:-1]
        return ans