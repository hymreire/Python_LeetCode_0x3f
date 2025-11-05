# 309. Best Time to Buy and Sell Stock with Cooldown

# 方法1：记忆化搜索
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,h):
            if i<0:
                return -inf if h else 0
            if h:
                # 持有=买入或保留
                # 保留只考虑i-1有即可
                # 买入必须i-1无，i-1不可能卖出，因此i-2必须无
                return max(dfs(i-2,False)-prices[i],dfs(i-1,True))
            return max(dfs(i-1,False),dfs(i-1,True)+prices[i])
        return dfs(n-1,False)

# 方法2：递推方程
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        f=[[0]*2 for _ in range(n+2)]
        f[1][1]=-inf # 刻意空出2格表示-2和-1
        for i,p in enumerate(prices):
            f[i+2][0]=max(f[i+1][1]+p,f[i+1][0])
            f[i+2][1]=max(f[i+1][1],f[i][0]-p)
        return f[-1][0]

# 方法3：递推，空间优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre,f0,f1=0,0,-inf # pre用于存-2索引
        for p in prices:
            pre,f0,f1=f0,max(f0,f1+p),max(f1,pre-p)
        return f0