# 51. N-Queens

# 枚举选择
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        path=[0]*n # 缓存变量：记录所占列，覆盖制
        col=[False]*n # 记录该列是否被占用
        diag_lu=[False]*(2*n-1) # 记录行列和是否被占用，从0到2n-2共2n-1个
        diag_ru=[False]*(2*n-1) # 记录行列差是否被占用，从-n+1到n-1共2n-1个
        # 输入行号r，调整改行对应的列号c
        def dfs(r):
            if r==n:
                ans.append(["."*c+"Q"+"."*(n-c-1) for c in path])
                return
            for c,cf in enumerate(col):
                if not cf and not diag_lu[r+c] and not diag_ru[r-c]:
                    path[r]=c
                    col[c]=diag_lu[r+c]=diag_ru[r-c]=True
                    dfs(r+1)
                    col[c]=diag_lu[r+c]=diag_ru[r-c]=False
        dfs(0)
        return ans