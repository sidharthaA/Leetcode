class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        a = 0
        for i in nums:
            result.append(a + i)
            a += i
        return result