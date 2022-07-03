class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        l = 0
        for n in nums:
            duplicate.add(n)
            l = l + 1
            # print(l, duplicate)
            if len(duplicate) != l:
                return True
        return False