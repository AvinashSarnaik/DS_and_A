## use BFS --> for u --> v -- add u to first and v to second
## for v --> w add w back to first and so on.

## NEW CONCEPT --> GRAPH COLORING PROBLEM 
## color a node x and color the neighbors y ... if node is already colored x and we try to color it y then error.
## Rember to check if all nodes are colored or not

class Solution:
    
    def all_visited(self,set_flag,queue):
        
        for node,val in enumerate(set_flag):
            if val == -1:
                queue.append(node)
                set_flag[node]=0
                return False
        
        return True
            
    
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        queue = []
        
        set_flag = [ -1 for _ in graph ]
        
        queue.append(0)
        set_flag[0] = 0
        
        while queue or not self.all_visited(set_flag,queue):
            
            next_queue = []
            
            for u in queue:
                for v in graph[u]:
                    if set_flag[u] == set_flag[v]:
                        return False
                    if set_flag[v] == -1:
                        set_flag[v] = (set_flag[u]+1) % 2
                        next_queue.append(v)
            
            queue = next_queue
        
        return True
        