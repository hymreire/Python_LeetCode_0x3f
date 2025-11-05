# 1039. Minimum Score Triangulation of Polygon

# 方法1：记忆化搜索
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i,j):
            if i+1==j:
                return 0
            return min(dfs(i,k)+dfs(k,j)+values[i]*values[j]*values[k] for k in range(i+1,j)) # 这个循环是精髓
        return dfs(0,len(values)-1)

# 方法2：递推方程
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n=len(values)
        f=[[0]*n for _ in range(n)]
        # 这两个判断语句很有意思
        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                f[i][j]=min(f[i][k]+f[k][j]+values[i]*values[j]*values[k] for k in range(i+1,j))
        return f[0][n-1]


