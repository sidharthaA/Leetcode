# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         closest = float("infinity")
#         final = 0
#         nums.sort()
#         # print(nums)
#         for k in range(len(nums)):
#             if k > 0 and nums[k] == nums[k - 1]:
#                 continue
#             i, j = k + 1, len(nums) - 1
#             while i < j:
#                 # print(nums[k], nums[i], nums[j])
#                 total = nums[k] + nums[i] + nums[j]
#                 # print(abs(target - total))
#                 if abs(target - total) < closest:
#                     closest = abs(target - total)
#                     final = total
#                 if total < target:
#                     i += 1
#                 elif total > target:
#                     j -= 1
#                 else:
#                     i += 1
#                     while nums[i] == nums[i - 1] and i < j:
#                         i += 1
#         return final

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 100000
        n = len(nums)
        for i in range(n-2):
            x = nums[i] + nums[-2] + nums[-1]
            if x < target:
                if abs(x-target) < abs(ans-target):
                    ans = x
                continue
            y = nums[i] + nums[i+1] + nums[i+2]
            if y > target:
                if abs(y-target) < abs(ans-target):
                    ans = y
                break
            a=nums[i]
            k = i+1
            e = n-1
            while k < e:
                s = nums[k] + nums[e]
                if s==target-a:
                    return target
                if abs(s+a-target)<abs(ans-target):
                    ans=s+a
                if s < target-a:
                    k += 1
                else:
                    e -= 1
        return ans