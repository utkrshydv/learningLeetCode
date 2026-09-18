class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
       

        og = image[sr][sc]

        if og == color:
            return image

        def dfs(row, col):
            image[row][col] = color

            dir = [(-1, 0),(1,0), (0,-1), (0, 1)]

            for r, c in dir:
                new_row = row + r
                new_col = col + c

                if (0<= new_row < len(image) and 0 <= new_col < len(image[0]) and image[new_row][new_col] == og):
                    dfs(new_row, new_col)

        dfs(sr, sc)

        return image
        