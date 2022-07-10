class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-1]
        two = min(cost[-1] + cost[-2], cost[-2])
        for i in range(len(cost) - 3, -1, -1):
            two, one = min(cost[i] + one, cost[i] + two), two
        return min(one, two)
    
    
    # two = cost[-1]
    #     one = min(cost[-1] + cost[-2], cost[-2])
    #     for c in cost[-3::-1]:
    #         one, two = min(c + one, c + two), one
    #     return(min(one, two))