class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # result = []
        # a = 0
        # for i in nums:
        #     result.append(a + i)
        #     a += i
        # return result
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums