class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
#         hor = horizontalCuts
#         ver = verticalCuts
#         hor.append(h)
#         hor.append(0)
#         ver.append(w)
#         ver.append(0) 
#         ver.sort()
#         hor.sort()
#         maxCake = 0
        
#         for h in range(len(hor) - 1):
#             for v in range(len(ver) - 1):
#                 maxCake = max(maxCake, (hor[h + 1] - hor[h]) * (ver[v + 1] - ver[v]))
#         return maxCake % (pow(10,9) + 7)

        horizontalCuts.sort()
        verticalCuts.sort()
        
        mxHr = 0
        prev = 0
        for i in horizontalCuts:
            mxHr = max(mxHr, i-prev)
            prev = i
        mxHr = max(mxHr, h-horizontalCuts[-1])
        
        mxVr = 0
        prev = 0
        for i in verticalCuts:
            mxVr = max(mxVr, i-prev)
            prev = i
        mxVr = max(mxVr, w-verticalCuts[-1])
        
        return (mxHr * mxVr) % ((10 ** 9) + 7)