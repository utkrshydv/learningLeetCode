class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        
        if not(top <= bottom):
            return False

        row = (top + bottom)//2

        left, right = 0, columns - 1
        while left <= right:
            mid = (left +  right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
       
        
        
        
        
        
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True

        # return False