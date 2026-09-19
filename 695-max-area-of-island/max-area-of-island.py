class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            grid[row][col] = 0
            area = 1
            dirn = [(-1, 0), (1,0), (0, 1), (0, -1)]

            for r, c in dirn:
                new_r = row + r
                new_c = col + c

                if 0<= new_r < rows and 0<= new_c < cols and grid[new_r][new_c]==1:
                    area += dfs(new_r, new_c)

            return area



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area
        