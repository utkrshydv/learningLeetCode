class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0

        def dfs(row, col):
            grid[row][col] = "0"

            dir = [(1,0), (-1,0), (0,1), (0,-1)]

            for r, c in dir:
                new_r = row + r
                new_c = col + c

                if 0<= new_r < len(grid) and 0<= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island += 1
                    dfs(row, col)


        return island
        