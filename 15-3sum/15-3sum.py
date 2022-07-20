class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = set()
        # print(nums)
        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            target = 0 - nums[k]
            while i < j:
                # if nums[k] == nums[k + 1]:
                #     continue
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    output.add((nums[i], nums[j], nums[k]))
                    i += 1
        return output