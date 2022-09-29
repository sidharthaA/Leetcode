class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        # print(total)
        left = 0
        right = total - nums[0]
        for index in range(len(nums)):
            if left == right:
                return index
            if index < len(nums) - 1:
                left += nums[index]
                right -= nums[index + 1]
        return -1