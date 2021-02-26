class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        nums_sorted = sorted(nums)
        
        left = 0
        while left != len(nums) and nums_sorted[left] == nums[left]:
            left+=1
        
        right = len(nums)-1
        while right > 0 and nums_sorted[right] == nums[right]:
            right-=1
        
        if left == len(nums_sorted) or right == -1:
            return 0
        else:
            return right-left+1
        
        