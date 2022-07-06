class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        result = set()
        result.add(0)
        
        for i in range(len(nums)):
            nextDP = set()
            for j in result:
                nextDP.add(j)
                if nums[i] + j <= target:
                    nextDP.add(nums[i] + j)
                if target in result:
                    return True
            result = nextDP
        return False
            