class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = cost[-1]
        one = min(cost[-1] + cost[-2], cost[-2])
        for c in cost[-3::-1]:
            one, two = min(c + one, c + two), one
        return(min(one, two))