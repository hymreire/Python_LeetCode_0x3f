# 17. Letter Combinations of a Phone Number

MAPPING="","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)

        # 分类讨论
        if n==0:
            return []
        
        ans=[]
        path=[""]*n # 列表乘法，缓存字符列表

        # 回溯本质是递归（dfs，深度优先搜索），一般与循环和枚举相配合
        def dfs(i):
            # 边界条件
            if i==n:
                ans.append("".join(path)) # 列表转字符串，其中""是连接符
                return
            
            for c in MAPPING[int(digits[i])]: # 元组索引也是用方括号
                path[i]=c
                dfs(i+1) # 递降

        dfs(0)

        return ans