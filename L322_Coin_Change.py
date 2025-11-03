# 322. Coin Change

# 方法1：记忆化搜索
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 索引i，容量c，返回最小的可行组合的元素数量（基数）
        @cache
        def dfs(i,c):
            # 边界条件
            if i<0:
                return 0 if c==0 else inf
            if c<coins[i]: # 太大不选
                return dfs(i-1,c)
            return min(dfs(i-1,c),dfs(i,c-coins[i])+1) # 选或不选
        ans=dfs(len(coins)-1,amount)
        return ans if ans<inf else -1

# 方法2：递推方程
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        f=[[inf]*(amount+1) for _ in range(n+1)] # f[i][c]表示容量c下前i个种类的最小组合基数
        f[0][0]=0
        for i,x in enumerate(coins):
            for c in range(amount+1):
                if c<x:
                    f[i+1][c]=f[i][c] ## 索引需要匹配循环
                else:
                    f[i+1][c]=min(f[i][c],f[i+1][c-x]+1) ## 注意min()，不要用花括号 ## 索引需要匹配循环
        ans=f[n][amount]
        return ans if ans<inf else -1

# 方法3：滚动数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        f=[[inf]*(amount+1) for _ in range(2)]
        f[0][0]=0
        for i,x in enumerate(coins):
            for c in range(amount+1):
                if c<x:
                    f[(i+1)%2][c]=f[i%2][c]
                else:
                    f[(i+1)%2][c]=min(f[i%2][c],f[(i+1)%2][c-x]+1)
        ans=f[n%2][amount]
        return ans if ans<inf else -1

# 方法4：一维数组
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f=[0]+[inf]*amount
        for x in coins:
            for c in range(x, amount+1):
                f[c]=min(f[c],f[c-x]+1) ## 容量增大时，要么从之前的最小基数加币，要么保持不变
        ans=f[amount]
        return ans if ans<inf else -1