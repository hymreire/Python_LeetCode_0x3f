# 46. Permutations

# 枚举选择的方法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        path=[0]*n # 初始化一个可覆盖的缓存
        on_path=[False]*n # 初始化一个可覆盖的判断标记
        # 输入当前的位置，填入合法的数值
        def dfs(i):
            if i==n: # 边界条件一般就是遍历结束的指针位置
                ans.append(path.copy()) # 方法一定要加括号
                return # 终止符不能忘记
            for j,on in enumerate(on_path):
                if not on:
                    path[i]=nums[j] # 赋值是什么要看清
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False
        dfs(0)
        return ans