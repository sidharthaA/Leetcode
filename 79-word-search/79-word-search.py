class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(index, r, c):
            if (r, c) in visited:
                return False
            visited.add((r, c))
            if word[index] != board[r][c]:
                visited.remove((r, c))
                return False
            if index == len(word) - 1:
                return True
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if row >= 0 and row < rows and col >= 0 and col < cols:
                    if dfs(index + 1, row, col):
                        return True
            visited.remove((r, c))
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
                
                        
        