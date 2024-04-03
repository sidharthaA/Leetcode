class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 in nums:
                continue
            count = 1
            next_num = num + 1
            while next_num in nums:
                count += 1
                next_num += 1
            max_count = max(max_count, count)
        return max_count