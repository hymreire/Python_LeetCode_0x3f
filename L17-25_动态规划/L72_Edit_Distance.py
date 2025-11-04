# 72. Edit Distance

# 方法1：记忆化搜索
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        @cache
        def dfs(i,j): # 将i:转换为j:的最小操作数 # 指针指向字符
            if i<0: # word1前缀空，需补0:j+1前缀
                return j+1
            if j<0: # word2前缀空，需删0:i+1前缀
                return i+1
            if word1[i]==word2[j]: # 匹配，不用操作，指针往前
                return dfs(i-1,j-1)
            # 不匹配，要么删除，要么插入，要么补上
            return min(dfs(i-1,j),dfs(i,j-1),dfs(i-1,j-1))+1
        return dfs(m-1,n-1)

# 方法2：递推方程
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        f=[[0]*(n+1) for _ in range(m+1)] # f[i][j]是:i到:j的最小操作数
        f[0]=list(range(n+1)) # w1空则插入w2的全部字符
        for i,x in enumerate(word1):
            f[i+1][0]=i+1 # w2空则删除w1全部字符 ## 初始化一定是要给后面使用的
            for j,y in enumerate(word2):
                f[i+1][j+1]=f[i][j] if x==y else min(f[i][j+1],f[i+1][j],f[i][j])+1
        return f[m][n]

# 方法3：滚动数组
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        f=[list(range(n+1)),[0]*(n+1)] # list()，圆括号不是方括号 # m,n的含义弄懂而不是硬背
        for i,x in enumerate(word1):
            f[(i+1)%2][0]=i+1
            for j,y in enumerate(word2):
                f[(i+1)%2][j+1]=f[i%2][j] if x==y else min(f[i%2][j+1],f[(i+1)%2][j],f[i%2][j])+1
        return f[m%2][n]

# 方法4：一维数组
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word2)
        f=list(range(n+1)) # 初始化f[0][j]
        for i,x in enumerate(word1):
            pre=f[0]
            f[0]+=1
            for j,y in enumerate(word2):
                tmp=f[j+1]
                f[j+1]=pre if x==y else min(pre,f[j],f[j+1])+1
                pre=tmp # 更新
        return f[-1]