class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [math.inf] * (len(nums))
        for i, num in enumerate(nums):
            ans[i] = nums[num]
        return ans