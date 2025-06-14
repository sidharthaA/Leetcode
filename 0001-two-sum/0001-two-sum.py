class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     tracker = {}
    #     for i, num in enumerate(nums):
    #         if num not in tracker:
    #             tracker[target - num] = i
    #         else:
    #             return [i, tracker[num]]

    # '''
    # Time Complexity: O(n) — single pass through the list.
    # Space Complexity: O(n) — for the hash map.
    # '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentary = {}
        for i, num in enumerate(nums):
            if num in complimentary:
                return [i, complimentary[num]]
            complimentary[target - num] = i
        return []