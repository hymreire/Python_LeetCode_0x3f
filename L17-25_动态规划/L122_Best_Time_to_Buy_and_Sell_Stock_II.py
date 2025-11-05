# 122. Best Time to Buy and Sell Stock II

# 方法1：记忆化搜索
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,h): # i天h状态最多赚钱数量
            if i<0: # 边界条件<0（默认0天还可以亏钱）
                return -inf if h else 0
            if h:
                return max(dfs(i-1,False)-prices[i],dfs(i-1,True)) # 买入则亏钱
            return max(dfs(i-1,True)+prices[i],dfs(i-1,False)) # 卖出则赚钱
        return dfs(n-1,False)

# 方法2：递推方程
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        f=[[0]*2 for _ in range(n+1)]
        f[0][1]=-inf
        for i,x in enumerate(prices):
            # 由于prices前面有用于初始化值的占位符号
            # 因此prices只好比f索引差一位
            f[i+1][0]=max(f[i][0],f[i][1]+prices[i]) 
            f[i+1][1]=max(f[i][0]-prices[i],f[i][1])
        return f[n][0]

# 方法3：递推，空间优化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0,f1=0,-inf
        for p in prices: # 这里不要用enumerate
            f0,f1=max(f0,f1+p),max(f0-p,f1)
        return f0