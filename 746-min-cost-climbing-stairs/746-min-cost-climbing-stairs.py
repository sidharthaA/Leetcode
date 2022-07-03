class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = cost[-1]
        one = min(cost[-1] + cost[-2], cost[-2])
        print(one, two)
        for i in cost[-3::-1]:
            one, two = min(i + one, i + two), one
        return min(one, two)