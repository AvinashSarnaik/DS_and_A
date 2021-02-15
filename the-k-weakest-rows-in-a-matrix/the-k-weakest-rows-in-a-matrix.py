class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        pq = []
        
        # 0(m*n*log(n))
        
        for idx,row in enumerate(mat):            # m
            soldiers = sum(row)                   # n
            heapq.heappush(pq,(soldiers,idx))     # log(m)
        
        weakest = []
        
        # O(k * log m)
        for _ in range(k):
            weakest.append(heapq.heappop(pq)[1])
        
        return weakest
        
        