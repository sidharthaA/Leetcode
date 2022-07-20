class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        n = nums
        for i in range(len(n) -1, 0, -1):
            # print(i)
            if n[i] <= n[i - 1]:
                continue
            else:
                pivot = i
                break
        # print("pivot=",pivot)
        if pivot == 0:
            nums = n.sort()
        # print(n)
        for i in range(len(n) - 1, pivot - 1, -1):
            # print("inside", n[i])
            if n[pivot - 1] < n[i]:
                # print("deep inside",n[pivot - 1], n[i], "pivot-1=", pivot-1)
                n[pivot - 1], n[i] = n[i], n[pivot - 1]
                break
        # print(n)
        n[pivot: len(n)] = sorted(n[pivot: len(n)])
        # print(n)
        nums = n