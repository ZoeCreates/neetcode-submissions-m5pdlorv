class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding windows 
        
        l = 0 
        char_set= set()
        max_len = 0 

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            
            char_set.add(s[r])
            max_len = max(max_len, r-l+1)
        
        return max_len 