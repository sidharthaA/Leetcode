class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # @lru_cache(None)
        # rcur = startRow
        # ccur = startColumn
        # global count
        # count = 0
        # def dp(move, rcur, ccur):
        #     global count
        #     if move < 0:
        #         return 0
        #     if rcur >= m or ccur >= n or rcur < 0 or ccur < 0:
        #         return 1
        #     else:
        #         # move -= 1
        #         # directions = [[rcur + 1, ccur], [rcur - 1, ccur], [rcur, ccur + 1], [rcur, ccur - 1]]
        #         for r, c in directions:
        #             # print("r:", r, "c:", c, "count:", count, "moves left:", move)
        #             flag = dp(move - 1, rcur + r, ccur + c)
        #             if not flag: 
        #                 continue
        #             if flag:
        #                 count += 1
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # dp(maxMove, rcur, ccur)
        # return count % (10**9 + 7)
    
    
    
        @lru_cache(None)
        def moves(move,row,col):
            if row==m or row<0 or col<0 or col==n:
                return 1
            if move==0:
                return 0
            move-=1

            return (moves(move,row+1,col)+moves(move,row,col+1)+moves(move,row-1,col)+moves(move,row,col-1))%((10**9)+7)


        return moves(maxMove,startRow,startColumn)