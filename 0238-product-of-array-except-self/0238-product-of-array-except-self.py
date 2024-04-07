class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        prod = 1
        for num in nums:
            before.append(prod)
            prod *= num
        prod = 1
        c = len(nums) -1
        for num in nums[::-1]:
            before[c] *= prod
            prod *= num
            c -= 1
        return before