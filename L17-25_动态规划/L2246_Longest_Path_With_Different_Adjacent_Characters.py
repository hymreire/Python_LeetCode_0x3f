# 2246. Longest Path With Different Adjacent Characters

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n=len(parent)
        g=[[] for _ in range(n)]
        for i in range(1,n):
            g[parent[i]].append(i)
        ans=0
        def dfs(x): # x的单根最长路径
            nonlocal ans
            max_len=0 # 第一支先算单根长度
            for y in g[x]:
                len_=dfs(y)+1 # y分支的长度（不考虑满足条件）
                if s[x]!=s[y]:
                    ans=max(ans,max_len+len_) # 满足条件考虑两个分支最大值
                    max_len=max(max_len,len_) # 更新单根最大路径
            return max_len
        dfs(0)
        return ans+1 # 最后算上根节点（前面只算了边长）