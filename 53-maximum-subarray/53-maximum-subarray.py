class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
    # brute force O(n^3)
        
        # maxCount = float("-inf")
        # for left in range(len(nums)):
        #     for right in range(len(nums)):
        #         count = 0
        #         for val in range(left, right + 1):
        #             count += nums[val]
        #             maxCount = max(count, maxCount)
        # return maxCount
        
    # brute force O(n^2)
        
        # maxCount = float("-inf")
        # for left in range(len(nums)):
        #     count = 0
        #     for right in range(left, len(nums)):
        #         count += nums[right]
        #         maxCount = max(count, maxCount)
        # return maxCount
        
    # greedy approach O(n)
    
        maxCount = float("-inf") if max(nums) >= 0 else max(nums)
        count = 0
        for val in range(len(nums)):
            count += nums[val]
            if count < 0:
                count = 0
            else:
                maxCount = max(count, maxCount)
        return maxCount