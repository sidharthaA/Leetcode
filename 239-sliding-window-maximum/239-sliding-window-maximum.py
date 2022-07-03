class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        max_array = []
        left_p = 0
        right_p = 0

        while right_p < len(nums):
            while queue and nums[queue[-1]] < nums[right_p]:
                queue.pop()
            queue.append(right_p)

            if left_p > queue[0]:
                queue.popleft()

            if right_p + 1 >= k:
                max_array.append(nums[queue[0]])
                left_p += 1

            right_p += 1

        return max_array