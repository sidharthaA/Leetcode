class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        fresh, time = 0, 0
        q = deque()
          
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: fresh += 1
                if grid[row][col] == 2: q.append([row, col])
            
        while q and fresh > 0:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append([r, c])
            time += 1
        return time if fresh == 0 else -1
                