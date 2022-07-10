class Solution:
    def rob(self, nums: List[int]) -> int:
        def repeat(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob2, rob1 = max(n + rob1, rob2), rob2
            return rob2
        val1 = repeat(nums[:-1])
        val2 = repeat(nums[1:])
        return max(nums[0], val1, val2)