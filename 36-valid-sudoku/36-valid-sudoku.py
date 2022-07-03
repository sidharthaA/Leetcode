class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            count = 0
            column = []
            if row % 3 == 0:
                boxSet1 = []
                boxSet2 = []
                boxSet3 = []
            for i in range(9):
                if board[i][row] == "." and board[row][i] == "." and i != 8:
                    continue
                item = board[row][i]
                if item != ".":
                    count = count + 1                
                if i == 8:
                    if len(set(board[row])) - count != 1:
                        return False
                if board[i][row] != ".":
                    column.append(board[i][row])
                if board[row][i] != ".":
                    if i < 3:
                        boxSet1.append(item)
                    elif i > 2 and i < 6:
                        boxSet2.append(item)
                    elif i > 5:
                        boxSet3.append(item)
            if len(set(column)) != len(column):
                return False
            if row % 3 == 2:
                if len(set(boxSet1)) != len(boxSet1) or len(set(boxSet2)) != len(boxSet2) or len(set(boxSet3)) != len(boxSet3):
                    return False
        return True
                
                
                