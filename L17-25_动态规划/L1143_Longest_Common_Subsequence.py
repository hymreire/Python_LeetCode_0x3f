# 1143. Longest Common Subsequence

# 方法1：记忆化搜索
# 我觉得就是从后往前搜，匹配上就加1，匹配不上就继续往前
# 递归正好将所有的情况都匹配到了
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        @cache
        def dfs(i,j):
            # 边界条件
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return dfs(i-1,j-1)+1
            return max(dfs(i-1,j),dfs(i,j-1))
        return dfs(m-1,n-1)

# 方法2：递推方程
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        f=[[0]*(n+1) for _ in range(m+1)]
        for i,x in enumerate(text1):
            for j,y in enumerate(text2):
                f[i+1][j+1]=f[i][j]+1 if x==y else max(f[i+1][j],f[i][j+1])
        return f[m][n]

# 方法3：滚动数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        f=[[0]*(n+1) for _ in range(2)]
        for i,x in enumerate(text1):
            for j,y in enumerate(text2):
                f[(i+1)%2][j+1]=f[i%2][j]+1 if x==y else max(f[i%2][j+1],f[(i+1)%2][j])
        return f[m%2][n]

# 方法4：一维数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        f=[0]*(len(text2)+1)
        for x in text1: # 在这个索引下所有一维变量视为i
            pre=0 # f[i][0]
            for j,y in enumerate(text2):
                tem=f[j+1] # f[i][j+1]
                # 分类讨论
                # f[i+1][j+1]=
                # f[i][j]+1
                # max(f[i][j+1],f[i+1][j])
                f[j+1]=pre+1 if x==y else max(f[j],f[j+1])
                pre=tem # f[i][j+1]
        return f[-1]