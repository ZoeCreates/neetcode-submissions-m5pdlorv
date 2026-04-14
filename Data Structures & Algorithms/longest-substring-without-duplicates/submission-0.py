class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        char_set = set()
        max_len = 0 

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l+=1
             
            
            char_set.add(s[i])
            max_len = max(max_len, i-l+1)
        
        return max_len