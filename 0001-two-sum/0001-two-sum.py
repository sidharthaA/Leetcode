class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for pos, num in enumerate(nums):
            if num in map:
                return [map[num], pos]
            map[target - num] = pos
        