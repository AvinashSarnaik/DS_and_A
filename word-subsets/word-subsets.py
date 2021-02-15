class Solution:
    
    def check_freq(self,a_freq,dest_freq):
        for char in dest_freq:
            if a_freq[char] < dest_freq[char]:
                return False
        return True
    
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        dest_freq = { chr(num):0 for num in range(97,123) }
        result = []
        
        for b in B:
            
            b_freq = { chr(num):0 for num in range(97,123) }
            for char in b:
                b_freq[char] += 1
                
            for char in dest_freq:
                dest_freq[char] = max(dest_freq[char],b_freq[char])
        
        for a in A:
            
            a_freq =  { chr(num):0 for num in range(97,123) }
            for char in a:
                a_freq[char] += 1
            
            if self.check_freq(a_freq, dest_freq):
                result.append(a)
        
        return result
            
            
                