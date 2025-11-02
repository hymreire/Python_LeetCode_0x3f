# 77. Combinations

# 方案一：枚举选择
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        # 从i开始往下选取剩余的数
        def dfs(i):
            d=k-len(path) # 剩余这么多数
            # 边界条件，不剩余就结束
            if d==0:
                ans.append(path.copy())
                return
            for j in range(i,d-1,-1): # 从[1,d-1]，至少留够d-1个数给后面选择
                path.append(j)
                dfs(j-1) # 递降
                path.pop() # 有选必有撤
        dfs(n)
        return ans

# 方案二：选或不选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i):
            d=k-len(path)
            if d==0:
                ans.append(path.copy())
                return
            # 余量充足，可以不选
            if i>d:
                dfs(i-1)
            # 选
            path.append(i)
            dfs(i-1)
            path.pop() # 有选必有撤
        dfs(n)
        return ans