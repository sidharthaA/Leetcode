class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        final = 0
        maxVal = 0
        for l in height:
            left.append(maxVal)
            if l > maxVal:
                maxVal = l
        maxVal = 0
        for r in range(len(height) - 1, -1, -1):
            temp = min(left[r], maxVal) - height[r]
            if temp >= 0:
                final += temp
            if height[r] > maxVal:
                maxVal = height[r]
        return final
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         heights = height
#         # start = 0
#         # end = 1
#         # count = 0
#         # while end < len(height):
#         #     count1 = 0
#         #     if height[end] < height[start]:
#         #         x = max(height[end:])
#         #         if x > height[start]:
#         #             count1 = count1 + height[start] - height[end]
#         #         else:
#         #             if end != len(height) - 1:
#         #                 count1 = count1 + height[start] - height[end] -(height[start] - x)
#         #         if end < len(height) - 1:
#         #             end = end + 1
#         #         else:
#         #             break
#         #     else:
#         #         count = count + count1
#         #         start = end
#         #         end = end + 1
#         # return count
        
#         res = 0
#         max_left = max_right = 0        
#         i, j = 0, len(heights) - 1
#         while i <= j:
#             if max_left <= max_right: # add left
#                 amount = max_left - heights[i]
#                 res = res + amount if amount > 0 else res
#                 max_left = max(max_left, heights[i])
#                 i += 1
#             else: # add right
#                 amount = max_right - heights[j]
#                 res = res + amount if amount > 0 else res
#                 max_right = max(max_right, heights[j])
#                 j -= 1
    
#         return res