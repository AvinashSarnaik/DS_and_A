class Solution:
    @staticmethod
    def swap( nums, curr, dest):
        if nums[curr] == nums[dest]:
            return
        nums[dest] , nums[curr] = nums[curr] , nums[dest]
        if nums[curr] == 0 or curr == nums[curr] - 1 :
            return
        Solution.swap(nums, curr, nums[curr] -1)
        
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_val = len(nums)
        
        for idx in range(len(nums)):
            if nums[idx] > max_val or nums[idx] < 0:
                nums[idx] = 0
        print(nums)
        for idx, value in enumerate(nums):
            if value == 0 or idx == value-1:
                continue
            Solution.swap(nums,idx,value-1)
                
        print(nums)
        for idx, value in enumerate(nums):
            if idx+1 != value:
                return idx+1
            
        return max_val+1
        
        
        