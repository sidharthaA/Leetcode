class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [i for i in nums]
        # for i in range(len(nums) - 3, -1, -1):
        #     for j in range(i + 2, len(nums)):
        #         dp[i] = max(dp[i], nums[i] + dp[j])
        # return max(dp)
        rob1, rob2 = 0, 0
        for n in nums:
            rob2, rob1 = max(n + rob1, rob2), rob2
        return rob2