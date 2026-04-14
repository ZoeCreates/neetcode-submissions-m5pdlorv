class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        max_len = 0
        max_freq = 0 
        dic = {}
    

        for r in range(len(s)):
            #更新当前字符的频率
            dic[s[r]] = 1 + dic.get(s[r],0)

            # 优化：记录当前窗口中最高的频率
            max_freq = max(max_freq, dic[s[r]])


            while (r-l+1)-max_freq > k:
                dic[s[l]] -=1
                l +=1
            
            max_len = max(max_len,r-l+1)
        
        return max_len


        