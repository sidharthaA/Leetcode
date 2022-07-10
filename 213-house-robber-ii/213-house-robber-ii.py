class Solution:
    def rob(self, nums: List[int]) -> int:
        def repeat(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob2, rob1 = max(n + rob1, rob2), rob2
            return rob2
        return max(nums[0], repeat(nums[:-1]), repeat(nums[1:]))