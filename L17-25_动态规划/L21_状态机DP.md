# 状态机DP
买卖股票问题：
```python
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
```

冷冻期：
```python
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
```

至多交易：
```python
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
```