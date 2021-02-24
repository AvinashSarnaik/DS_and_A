## we can go to end of first row and check -- start @ top right corner
## IF target greater than this value then we go to lower row (row+1)
## ELSE target less than this then move to right column (col-1)

## runtime -- O(m+n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        
        if matrix == None:
            return None
        
        while row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                row+=1
            else:
                col-=1
        
        return False