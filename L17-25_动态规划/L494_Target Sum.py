# 494. Target Sum

# 选或不选

# 方法1：记忆递归（记忆化搜索）
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

# 方法2：递推方程
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tem=sum(nums)-abs(target)
        if tem<0 or tem%2: # 是否整除2作为一个判断标准
            return 0
        cap=tem//2
        n=len(nums)

        # 初始化递推表f[i][c]，索引i之前的元素集合，和为容量c的组合数
        # 需要给边界条件索引0和容量0留够位置，所以下面初始化大小时是双+1
        f=[[0]*(cap+1) for _ in range(n+1)]
        # f[0][0]表示：索引0之前的元素集合（没元素，空集），和为容量0的组合数（1种，空集）
        # 边界条件
        f[0][0]=1

        for i,x in enumerate(nums): # 用enumerate同时枚举索引和数值
            for c in range(cap+1):
                if c<x:
                    f[i+1][c]=f[i][c]
                else: # 由于没有终止符，所以此处必须else
                    f[i+1][c]=f[i][c]+f[i][c-x]
        
        return f[n][cap] # 看清楚返回值很重要

# 方法3：滚动数组优化空间
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tem=sum(nums)-abs(target)
        if tem<0 or tem%2:
            return 0
        cap=tem//2
        n=len(nums)
        f=[[0]*(cap+1) for _ in range(2)] # 多维列表不能*初始化
        f[0][0]=1 # 一定要初始化
        for i,x in enumerate(nums):
            for c in range(cap+1):
                if c<x:
                    f[(i+1)%2][c]=f[i%2][c]
                else:
                    f[(i+1)%2][c]=f[i%2][c]+f[i%2][c-x]
        return f[n%2][cap]

# 方法4：一维数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tem=sum(nums)-abs(target)
        if tem<0 or tem%2:
            return 0
        cap=tem//2
        # f[c]是缓存递推表，表示i索引时，和为容量c的组合数
        f=[1]+[0]*cap
        for x in nums:
            for c in range(cap,x-1,-1):
                f[c]+=f[c-x]
        return f[cap]