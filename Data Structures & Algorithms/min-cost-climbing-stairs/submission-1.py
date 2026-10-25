class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        '''
        1. Recursion（纯递归 / 暴力搜索）计算方向：自顶向下（Top-Down）。
从目标起点（第 0/1 阶）出发，不断向下拆分出子问题 dfs(i+1) 和 dfs(i+2)，直到碰底（到达顶端）。核心缺点：有大量重复计算（Overlapping Subproblems）。
比如算 dfs(0) 会调用 dfs(1) 和 dfs(2)；算 dfs(1) 又会调用 dfs(2) 和 dfs(3)。其中 dfs(2) 被重复调用并完整计算了多次。时间复杂度：$O(2^n)$（指数级，节点数随着深度呈二叉树爆炸增长，极易超时）。


2. Dynamic Programming Top-Down（带备忘录的 DP / 记忆化搜索）计算方向：自顶向下（Top-Down）。
依然保持了递归的过程和逻辑，但在纯递归的基础上加了一个 memo 数组（备忘录）。核心改进：剪枝 / 缓存。
当第一次算出 dfs(i) 的结果时，把它存进 memo[i] 中。下一次再遇到同样的 i 时，触发 if memo[i] != -1: return memo[i]，直接返回答案。时间复杂度：$O(n)$（每个状态 $i$ 只被真正计算一次）。
        '''
        
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0 
            if memo[i]!= -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return memo[i]

        return min(dfs(0),dfs(1))