# 188. Best Time to Buy and Sell Stock IV

# 方法1：记忆化搜索
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,j,h):
            if j<0:
                return -inf
            if i<0:
                return -inf if h else 0
            if h:
                return max(dfs(i-1,j,True),dfs(i-1,j-1,False)-prices[i])
            return max(dfs(i-1,j,True)+prices[i],dfs(i-1,j,False)) # 买卖只算一次，有买必有卖
        return dfs(n-1,k,False)

# 方法2：递推方程
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        f=[[[-inf]*2 for _ in range(k+2)] for _ in range(n+1)]
        for j in range(1,k+2): # j=0初始化为-inf，避免-1越界
            f[0][j][0]=0 # 0天j次0收益
        for i,p in enumerate(prices):
            for j in range(1,k+2): # j=0初始化为-inf，避免-1越界
                f[i+1][j][0]=max(f[i][j][0],f[i][j][1]+p)
                f[i+1][j][1]=max(f[i][j-1][0]-p,f[i][j][1])
        return f[-1][-1][0]

# 方法3：递推，空间优化
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f=[[-inf]*2 for _ in range(k+2)] # 切记k+2
        for j in range(1,k+2):
            f[j][0]=0
        for p in prices:
            for j in range(1,k+2):
                f[j][0]=max(f[j][0],f[j][1]+p)
                f[j][1]=max(f[j-1][0]-p,f[j][1]) # 买入卖出收益分析
        return f[-1][0]