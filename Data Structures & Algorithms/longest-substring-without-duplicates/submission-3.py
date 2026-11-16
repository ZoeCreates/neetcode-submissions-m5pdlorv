class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        char_set = set()
        max_len = 0

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len,r-l+1)
                r+=1
            else:
                char_set.remove(s[l])
                l+=1
                
            
            
        
        return max_len 

      
        



