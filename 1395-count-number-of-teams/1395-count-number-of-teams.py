class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        def left(sol):
            lCountLess, lCountGreater = 0, 0
            for r in range(sol):
                if rating[r] < rating[sol]:
                    lCountLess += 1
                if rating[r] > rating[sol]:
                    lCountGreater += 1
            return lCountLess, lCountGreater
        def right(sol):
            rCountLess, rCountGreater = 0, 0
            for r in range(sol + 1, len(rating)):
                if rating[r] < rating[sol]:
                    rCountLess += 1
                if rating[r] > rating[sol]:
                    rCountGreater += 1
            return rCountLess, rCountGreater
        
        for soldier in range(1, len(rating) - 1):
            lCountLess, lCountGreater = left(soldier)
            rCountLess, rCountGreater = right(soldier)
            count += lCountLess * rCountGreater + lCountGreater * rCountLess
        return count
            