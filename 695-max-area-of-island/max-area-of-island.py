class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        def dfs(row, col):
            grid[row][col] = 0
            area = 1

            dir = [(1,0), (-1,0), (0, 1), (0,-1)]

            for r, c in dir:
                new_r = row + r
                new_c = col + c

                if 0<= new_r < len(grid) and 0<=new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    area += dfs(new_r, new_c)

            return area


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    max_area = max(max_area, dfs(row, col))
        

        return max_area