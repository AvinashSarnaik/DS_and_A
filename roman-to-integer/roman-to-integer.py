class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        
        last_digit = dictionary[ s[-1] ]
        
        integer = 0
        
        for num in reversed(s):
            curr_digit = dictionary[num]
            if last_digit > curr_digit:
                integer -= curr_digit
            else:
                integer += curr_digit
            
            last_digit=curr_digit
        
        return integer
            
            