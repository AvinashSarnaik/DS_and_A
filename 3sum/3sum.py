class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_set = set(nums)
        nums_dict = { num:0 for num in nums }
        for num in nums:
            nums_dict[num] += 1        
        
        result = set()
        
        for i in nums_set:
            for j in nums_set:
                if (-i-j) in nums_set:   
                    
                    k = -i-j
                    
                    nums_dict[i] -= 1
                    nums_dict[j] -= 1
                    nums_dict[k] -= 1
                    
                    if nums_dict[i] > -1 and nums_dict[j] > -1 and nums_dict[k] > -1:
                        current = [i,j,k]
                        current.sort()
                        current = "_".join([ str(num) for num in current])
                        result.add(current)
                    
                    nums_dict[i] += 1
                    nums_dict[j] += 1
                    nums_dict[k] += 1
        
        result_list = []
        for res in result:
            res = [ int(chunk) for chunk in res.split("_") ]
            result_list.append(res)
            
        return result_list
                    
                    
                        
                    