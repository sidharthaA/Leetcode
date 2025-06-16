class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        low = nums[0]
        res = -1
        for high in nums:
            low = min(low, high)
            if high > low:
                res = max(res, high - low)
        return res