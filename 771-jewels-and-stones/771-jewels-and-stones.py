class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         stone_count = {}
#         for i in stones:
#             if i in stone_count:
#                 stone_count[i] += 1
                
#         stones = set(stones)
        # print(stones)
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count