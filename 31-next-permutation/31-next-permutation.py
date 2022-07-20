class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        n = nums
        for i in range(len(n) -1, 0, -1):
            if n[i] <= n[i - 1]:
                continue
            else:
                pivot = i
                break
        if pivot == 0:
            nums = n.sort()
        for i in range(len(n) - 1, pivot - 1, -1):
            if n[pivot - 1] < n[i]:
                n[pivot - 1], n[i] = n[i], n[pivot - 1]
                break
        n[pivot: len(n)] = sorted(n[pivot: len(n)])
        nums = n