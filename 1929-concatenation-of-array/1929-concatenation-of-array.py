class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [math.inf] * 2 * len(nums)
        # for i, num in enumerate[nums]:
        #     ans[i] = num
        #     ans[i + len(nums)] = num
        # return ans
        
        return nums + nums