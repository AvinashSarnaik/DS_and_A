from bisect import bisect_left, bisect_right , insort_left, insort_right

class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = { chr(num):0 for num in range(97,123) }
        for char in S:
            freq[char] += 1
        freq_sorted = [ (v,k) for k,v in freq.items() if v != 0]
        freq_sorted.sort()
        
        result = ""
        while len(freq_sorted) >= 2:
            first 	= freq_sorted.pop()
            second 	= freq_sorted.pop()
            result += first[1]
            result += second[1]
            first = (first[0]-1, first[1])
            second = (second[0]-1, second[1])
            if first[0]:
                insort_left(freq_sorted, first)
            if second[0]:
                insort_left(freq_sorted, second)
        
        if freq_sorted:
            result += freq_sorted[0][1] * freq_sorted[0][0]
        
        failed = False
        last_char = result[0]
        for char in result[1:]:
            if char == last_char:
                failed = True
            last_char = char
        
        return result if not failed else ""
