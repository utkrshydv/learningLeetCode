class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        og = image[sr][sc]

        if og == color:
            return image

        def dfs(row, col):
            image[row][col] = color

            dir = [(-1, 0), (1,0), (0,-1), (0,1)]

            for r, c in dir:
                new_r, new_c = row + r, col + c

                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]) and image[new_r][new_c] == og:
                    dfs(new_r, new_c)

        dfs(sr, sc)

        return image