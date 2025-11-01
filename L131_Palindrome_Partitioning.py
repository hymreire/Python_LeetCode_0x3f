# 方法一：选或不选：对于每个i，决定是否在它后面进行切分
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        path=[]

        # start——>i 切分后是否为回文串
        def dfs(i,start):
            if i==n: # 边界条件
                ans.append(path.copy())
                return # 终止符
            # 不选
            if i<n-1:
                dfs(i+1,start)
            # 选
            t=s[start:i+1]
            if t==t[::-1]: # 是回文串
                path.append(t) # 加入当前切割组合
                dfs(i+1,i+1) # 递降
                path.pop() # 有选必有撤
        
        dfs(0,0)

        return ans

# 方法二：枚举选择
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        path=[]
        def dfs(i):
            # 边界条件
            if i==n:
                ans.append(path.copy())
                return # 终止符
            for j in range(i,n): # 切片范围，小心数组越界
                # 选择
                t=s[i:j+1]
                if t==t[::-1]: # 判断回文
                    path.append(t)
                    dfs(j+1) # 递降
                    path.pop() # 有选必有撤
        dfs(0)
        return ans