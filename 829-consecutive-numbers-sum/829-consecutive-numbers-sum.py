class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # count = 1
        # total = 0
        # i = n //2 + 1
        # total = i
        # j = i - 1
        # while j > 0:
        #     total += j
        #     if total < n:
        #         j -= 1
        #         continue
        #     elif total > n:
        #         total -= i
        #         i -= 1
        #         j -= 1
        #     elif total == n and i != j:
        #         count += 1
        #         total -= i
        #         i -= 1
        #         j -= 1
        # return count
    
    # solution from discussions: https://leetcode.com/problems/consecutive-numbers-sum/discuss/1767911/Python-Simple-6-lines-solution
        ans, sumNum, cnt = 1, 1, 2
        while sumNum < n:
            if sumNum % cnt == n % cnt: ans += 1
            sumNum += cnt
            cnt += 1
        return ans