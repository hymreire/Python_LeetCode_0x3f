# 494. Target Sum

# 方法：选或不选
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 推导公式是p+q=s,p-q=t——>q=(s-t)/2或p=(s-(-t))/2，
        # 归纳为(s-abs(t))/2，这样凑的数更小，可以优化程序
        tem=sum(nums)-abs(target) # 临时存一下s-t ## 一定要加绝对值，可以优化程序
        # 如果tem非双数，必然凑不出结果
        # 如果tem非整数，必然凑不出结果
        if tem<0 or tem%2!=0:
            return 0
        cap=tem//2 ## 加上整除提升精度
        # 输入：当前索引，剩余容量，输出：从0到当前索引能凑出容量的结果数量
        @cache ## 一定要有cache，可以大幅优化程序（这个真的可以快很多）
        def dfs(i,c):
            # 边界条件
            if i<0:
                return 1 if c==0 else 0
            # 判断条件（剪枝）
            if c<nums[i]:
                return dfs(i-1,c) ## 必须有return，否则白做递归
            # 选或不选的结果加起来就是所有的结果
            return dfs(i-1,c)+dfs(i-1,c-nums[i])
        return dfs(len(nums)-1,cap)