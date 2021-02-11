## CONCEPT --> WE CAN USE TWO POINTERS WHEN WE HAVE TWO POSITIONS TO FIX

## Brute force is to select two lines in n^2 and check the area to minimize it
## TWO POINTERS is to put pointer at start and end and go on optimizing it by moving the limiting end (smaller value) 
## in search for a better one

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        area = 0
        
        while start < end:
            height_idx = start if height[start] < height[end] else end
            area = max(area,height[height_idx] * (end-start))
            if height_idx == start:
                start += 1
            else:
                end -= 1
        
        return area