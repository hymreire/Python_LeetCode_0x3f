# 516. Longest Palindromic Subsequence

# 方法1：记忆化搜索
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return dfs(i+1,j-1)+2
            else:
                return max(dfs(i+1,j),dfs(i,j-1)) # 注意搜索顺序
        return dfs(0,len(s)-1)

# 方法2：递推方程
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        f=[[0] *n for _ in range(n)]
        for i in range(n-1,-1,-1): ## 必须从大往小枚举
            f[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    f[i][j]=f[i+1][j-1]+2
                else:
                    f[i][j]=max(f[i+1][j],f[i][j-1]) ## 从中间向两端扩散
        return f[0][-1]

# 方法3：递推，空间优化
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        f=[0]*(n)
        for i in range(n-1,-1,-1):
            f[i]=1 # f[i][i]
            pre=0 # f[i+1][i]
            for j in range(i+1,n):
                tmp=f[j]
                if s[i]==s[j]:
                    f[j]=pre+2 # 前缀的重置效应很重要
                else:
                    f[j]=max(f[j],f[j-1])
                pre=tmp
        return f[-1]