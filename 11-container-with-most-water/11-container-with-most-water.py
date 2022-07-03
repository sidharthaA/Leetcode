class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end, maxArea = 0, len(height) - 1, 0
        while start < end: 
            width = end - start
            length = min(height[start], height[end])
            
            if height[end] == length:
                end = end - 1
            else:
                start = start + 1
                
            if length * width > maxArea:
                maxArea = length * width
        return maxArea
    
#     /*
#     class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         start = 0
#         end = len(height) - 1
#         maxArea = 0
#         length = 0
#         length1 = 0
#         l = [0]
#         while start < end: 
#             width = end - start
#             # length1 = max(l)
#             if length > length1:
#                 length1 = length
#             length = min(height[start], height[end])
#             # l.append(length)
            
#             if height[start] == length:
#                 if end - start == 1:
#                     start = 0
#                     end = end - 1
#                 else:
#                     start = start + 1
#                 continue
#             if length * width > maxArea:
#                 maxArea = length * width
#             print(height[start], height[end])
#             print("area", length * (end - start))
#             if end - start == 1:
#                 start = 0
#                 end = end - 1
#             else:
#                 start = start + 1
#         return maxArea 