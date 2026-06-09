class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i] is the number of distinct ways to climb to stair i 
    
    # '''
    # 1. 针对小测试用例的“走捷径”（剪枝）LeetCode 在评测代码时，会运行很多组测试用例。
    # 其中一定会包含 n = 0 或 n = 1 这种最小边界情况。
    # 没有这一行时：代码需要老老实实地去初始化大小为 n + 1 的列表、给 dp[0] 和 dp[1] 赋值、跑一个 range(2, n+1) 的循环（虽然循环不执行），最后再返回。
    # 有这一行时：如果是 n = 0 或 n = 1，代码在第 4 行直接就 return 1 退出函数了。
    # 后面所有开辟内存空间、数组赋值的操作全部被提前拦截了。
    # 对于这些小用例，耗时直接降到了接近 0 毫秒。
    # 2. 规避了隐藏的数组越界崩溃（更重要）这行代码除了在微观上省时间，更核心的作用是保证了代码的健壮性。
    # 如果把这行代码删掉，当 n = 0 时，看看会发生什么：dp = [0] * (0 + 1) $\rightarrow$ 创建了一个长度只有 1 的列表：dp = [0]。
    # dp[0] = 1 $\rightarrow$ 没问题，修改了唯一的一个元素。dp[1] = 1 $\rightarrow$ 报错崩溃！ 
    # 因为 dp 只有下标 0，压根没有下标 1，程序会直接抛出 IndexError: list assignment index out of range。
    # '''
        
        if n <= 1:
            return 1
       
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] =1
        

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        