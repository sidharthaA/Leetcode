class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # result = []
        # a = 0
        # for i in nums:
        #     result.append(a + i)
        #     a += i
        # return result
        # replace nums starting from 2nd element with the sum of current and previous element
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums