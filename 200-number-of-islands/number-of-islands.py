class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            grid[row][col] = "0"

            dirn = [(-1, 0), (1,0), (0, -1), (0, 1)]

            for nr, nc in dirn:
                n_row = row + nr
                n_col = col + nc

                if 0<= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] == "1":
                    dfs(n_row, n_col) 



        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    islands += 1
                    dfs(row, col)        

        return islands