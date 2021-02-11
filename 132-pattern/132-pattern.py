## CONCEPT --> i (min) < j (max) < k (mid)
## we cANNOT KEEP TRACK OF J in anything so i==array and k is nearest greater stack ==== for j we can ONLY run condition by getting min of left (i) and nearest max on right (k)

## === we can get min which is i from min array
## === we can keep an increasing stack (top to bottom) of elements which are greater that min[idx] which will be our next nearest to i value k
## === for each element from last -1 to start try to find a j which is more than min[idx] and greater than stack top


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_list = []
        minimum = nums[0]
        
        for num in nums:
            min_list.append(minimum)
            minimum = min(minimum,num)
        
        stack = []
        stack.append(nums[-1])
        
        for idx in range(len(nums)-2,-1,-1):
            
            while stack and stack[-1] <= min_list[idx]:
                stack.pop()
            
            if nums[idx] > min_list[idx] and stack and nums[idx] > stack[-1]:
                return True
            
            if not stack or nums[idx] < stack[-1] :
                stack.append(nums[idx])
        
        return False
            
            