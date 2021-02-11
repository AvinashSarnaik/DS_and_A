### CONCEPT --> WE CAN APPLY KNOWN DP SOLUTION OF TOP-LEFT IN TWO PHASES FOR 4 DIRECTIONAL MOVEMENT

## We can take the BFS and push all ZERO value as zero and add neighbours
## BUT We can take DP in two loops
## LOOP 1 --> limit DP as Top and Left and go from top-left to bottom-right
## LOOP 2 --> limit DP as Bottom and Right and go from bottom-right to top-left

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[ float('inf') for _ in range(n)] for _ in range(m)] 
        
        dp[0][0] = 0 if matrix[0][0] == 0 else float('inf')
              
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    dp[r][c] = 0
                elif r == 0 :
                    if c > 0:
                        dp[r][c] = dp[r][c-1] + 1
                elif c == 0 :
                    if r > 0:
                        dp[r][c] = dp[r-1][c] + 1
                else:
                    dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if matrix[r][c]==0:
                    dp[r][c] = 0
                elif r == m-1:
                    if c < n-1:
                        dp[r][c] = min(dp[r][c], dp[r][c+1] + 1)
                elif c == n-1:
                    if r < m-1:
                        dp[r][c] = min(dp[r][c],dp[r+1][c] + 1)
                else:
                    dp[r][c] = min(dp[r][c],min(dp[r+1][c],dp[r][c+1]) + 1 )
        
        return dp
                