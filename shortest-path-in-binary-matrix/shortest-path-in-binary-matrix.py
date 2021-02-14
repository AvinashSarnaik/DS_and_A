## since we are asked a shortest path 
## let's use BFS

## FOR BFS --> use queue (priority queue if it is single source shortest path to all other nodes) for DFS we use recursive stack.

## CHECK VISITED needed --> from the look of it we can move backward 
## and we do not have gurantee that we reach grid[-1][-1] 
## so WE NEED TO USE VISITED to avoid looping back and forth.


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        last_r = len(grid) - 1
        last_c = len(grid[0]) - 1 
        
        if grid[last_r][last_c] == 1 or grid[0][0] == 1:
            return -1
        
        queue = []
        directions = ((0,1),(0,-1),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1))
        visited = set()
        
        if len(grid) == 1 and len(grid[0])==1:
            return 1
        else:
            queue.append((0,0))
            visited.add((0,0))
            
        steps = 1
        
        while queue:
            
            next_queue = []
            
            for current in queue:
                
                for r,c in ( (current[0]+d[0],current[1]+d[1]) for d in directions ) :
                    
                    if r < 0 or r > last_r or c< 0 or c > last_c \
                       or grid[r][c] == 1 or (r,c) in visited:
                        continue
                    elif r==last_r and c==last_c:
                        return steps+1
                    else:
                        next_queue.append((r,c))
                        visited.add((r,c))
            
            queue = next_queue
            steps+=1
        
        return -1
            
            
                    