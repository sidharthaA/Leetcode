class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        # print(nums)
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            target = 0 - nums[k]
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
        return output

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #         continue
        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = a + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res