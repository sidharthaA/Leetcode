class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        full_list = {i for i in range(1, n + 1)}
        return list(full_list.difference(nums_set))
