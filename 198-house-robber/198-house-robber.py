class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [i for i in nums]
        # print(dp)
        for i in range(len(nums) - 3, -1, -1):
            # print("i = ", i)
            for j in range(i + 2, len(nums)):
                # print("j = ", j)
                dp[i] = max(dp[i], nums[i] + dp[j])
                # print("dp[i] = ", dp[i])
        return max(dp)