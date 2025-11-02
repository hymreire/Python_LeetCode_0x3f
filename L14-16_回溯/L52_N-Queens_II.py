# 52. N-Queens II

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        # col=[0]*n # 这行忽略
        col_mark=[False]*n
        diag_lu=[False]*(2*n-1)
        diag_ru=[False]*(2*n-1)
        def dfs(r):
            nonlocal ans # 必须声明非局部
            if r==n:
                ans+=1
                return
            for c,cm in enumerate(col_mark):
                if not cm and not diag_lu[r+c] and not diag_ru[r-c]:
                    # col[r]=c # 这行忽略
                    col_mark[c]=diag_lu[r+c]=diag_ru[r-c]=True
                    dfs(r+1)
                    col_mark[c]=diag_lu[r+c]=diag_ru[r-c]=False
        dfs(0)
        return ans