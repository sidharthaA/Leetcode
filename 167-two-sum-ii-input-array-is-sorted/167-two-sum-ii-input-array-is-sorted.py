class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[end] > target - numbers[start]:
                end = end - 1
                continue
            if numbers[start] > target - numbers[end]:
                start = start + 1
                continue
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            start = start + 1