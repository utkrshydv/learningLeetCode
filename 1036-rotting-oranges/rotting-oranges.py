class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        dir = [(-1,0), (1,0), (0,1),(0,-1)]

        while q and fresh > 0:
            level_size = len(q)

            for _ in range(level_size):
                row, col = q.popleft()

                for dr, dc in dir:
                    new_row = row + dr
                    new_col = col + dc

                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        q.append((new_row, new_col)) 

            minutes += 1

        if fresh > 0:
            return -1

        return minutes     


        # r = len(grid)
        # c = len(grid[0])

        # q = deque()
        # f = 0
        # m = 0

        # for row in range(r):
        #     for col in range(c):
        #         if grid[row][col] == 2:
        #             q.append((row, col))
        #         elif grid[row][col] == 1:
        #             fresh += 1

        # dir = [(-1, 0), (1,0), (0,-1), (0, 1)]

        # while q and fresh > 0:
        #     level_size = len(q)

        #     for _ in range(level_size):
        #         row, col = q.popleft()

        #         for dr, dc in dir:
        #             new_r = row + dr
        #             new_c = col + dc

        #             if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1):
        #                 grid[new_row][new_col] = 2
        #                 fresh -= 1
        #                 q.append((new_row, new_col)) 

        #     minutes += 1

        # if fresh > 0:
        #     return -1

        # return minutes