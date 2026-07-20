class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True 
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] +=1 
            #新进来一个字符后，两边刚巧对齐了
            if s1Count[index] == s2Count[index]:
                matches +=1
            #新进来一个字符后，两边原本是对齐的，现在变不对齐了
            elif s1Count[index] +1 == s2Count[index]:
                matches -=1
            
            l_index = ord(s2[l]) - ord('a')
            s2Count[l_index] -= 1  # 频次减 1
            if s1Count[l_index] == s2Count[l_index]:
                matches += 1
            elif s1Count[l_index] - 1 == s2Count[l_index]:
                # 如果减完 1 之后刚好不相等了（原来是相等的），matches 需要减 1
                matches -= 1
                
            # 左指针向右移动，收缩窗口
            l += 1

        return matches == 26
            

            


        
        
        
        