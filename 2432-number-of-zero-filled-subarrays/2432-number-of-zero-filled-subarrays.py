# class Solution:
#     def zeroFilledSubarray(self, nums: List[int]) -> int:
#         count = 0
#         left, right = 0, 0
#         flag = False
#         while right < len(nums):
#             while right < len(nums) and nums[right] == 0:
#                 right += 1
#                 flag = True
#             if flag:
#                 n = right - left
#                 count += n * (n + 1) / 2
#                 flag = False
#                 right -= 1
#             right += 1
#             left = right
#         return int(count)

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        curr_zeros = 0
        for num in nums:
            if num == 0:
                curr_zeros += 1
                count += curr_zeros
            else:
                curr_zeros = 0
        return count