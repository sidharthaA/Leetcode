class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right, mid = 0 , length - 1, length // 2
        while left <= right:
            # print('left:', left, '\tright:', right, '\tmid:', mid)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            mid = (left + right) // 2
        return -1