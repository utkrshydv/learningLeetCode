class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        og_color = image[sr][sc]

        if og_color == color:
            return image

        def dfs(row, col):
            image[row][col] = color

            dir = [(-1,0), (1,0), (0,-1), (0, 1)]

            for dr, dc in dir:
                new_row = row + dr
                new_col = col + dc

                if(0<= new_row < len(image) and
                    0<= new_col < len(image[0]) and
                    image[new_row][new_col] == og_color):
                    dfs(new_row, new_col)
        
        dfs(sr, sc)

        return image
        