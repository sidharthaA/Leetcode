class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         nums_set = list(set(nums))
#         sum1 = 0
#         for i in nums_set:
#             sum1 += i
#         sum1 *= 2
        
        sum2 = 0
        for i in nums:
            sum2 = sum2 ^ i
        
        return sum2