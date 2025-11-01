

# 方法一：枚举选择
class Solution:
    # k是一个全局变量不要管
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        path=[]
        # 输入当前最大值i和剩余总和ls，输出剩余组合
        def dfs(i,ls):
            d=k-len(path)
            # 这里很巧妙，d=0时，l被夹逼为0
            if ls<0 or ls>(2*i-d+1)*d/2:
                return
            if d==0: # 加入列表一定要copy
                ans.append(path.copy())
                return
            for j in range(i,d-1,-1): # 范围遵循左闭右开
                path.append(j)
                dfs(j-1,ls-j) # ls才是动态变化量
                path.pop() # 弹出的方法一定要加括号
        dfs(9,n)
        return ans

# 方法二：选或不选
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(i,ls):
            d=k-len(path)
            # 这里很巧妙，d=0时，l被夹逼为0
            if ls<0 or ls>(2*i-d+1)*d/2: # 写判断条件时要细心不能写错符号
                return
            if d==0:
                ans.append(path.copy())
                return
            # 不选
            if i>d:
                dfs(i-1,ls)
            # 选
            path.append(i)
            dfs(i-1,ls-i)
            path.pop()
        dfs(9,n)
        return ans