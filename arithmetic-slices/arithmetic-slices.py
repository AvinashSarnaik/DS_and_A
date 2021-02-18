class Solution:
    
    def get_distinct(self,start,end):
        count = 0
        distinct = 1
        window = end - start + 1
        while window >= 3:
            count += distinct
            window -=1
            distinct +=1
        
        return count
            
        
    
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        if len(A) < 2:
            return 0
        
        start = 0
        end = 1
        sequences = 0
        
        while end != len(A):
            diff = A[end]-A[start]
            while end+1 < len(A)  and A[end] + diff == A[end+1]:
                end+=1
            sequences += self.get_distinct(start,end)
            start = end
            end += 1
            
        return sequences
        