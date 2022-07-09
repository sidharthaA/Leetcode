class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]for i in range(len(text1) + 1)]
        
        for pointer1 in range(len(text1) - 1, -1, -1):
            for pointer2 in range(len(text2) - 1, -1, -1):
                if text1[pointer1] == text2[pointer2]:
                    dp[pointer1][pointer2] = 1 + dp[pointer1 + 1][pointer2 + 1]
                else:
                    dp[pointer1][pointer2] = max(dp[pointer1 + 1][pointer2], dp[pointer1][pointer2 + 1])
        return dp[0][0]
    
#     class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
#         for pointer1 in range(len(text1) - 1, -1, -1):
#             for pointer2 in range(len(text2) - 1, -1, -1):
#                 if text1[pointer1] == text2[pointer2]:
#                     dp[pointer1][pointer2] = 1 + dp[pointer1 + 1][pointer2 + 1]
#                 else:
#                     dp[pointer1][pointer2] = max(dp[pointer1][pointer2 + 1], dp[pointer1 + 1][pointer2])
        
#         return dp[0][0]