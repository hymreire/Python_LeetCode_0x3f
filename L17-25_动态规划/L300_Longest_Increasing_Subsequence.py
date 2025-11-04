# 300. Longest Increasing Subsequence

# 方法1：记忆化搜索
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            res=0 # 前缀最长值
            for j in range(i):
                if nums[j]<nums[i]:
                    res=max(res,dfs(j))
            return res+1
        return max(dfs(i) for i in range(len(nums)))

# 方法2：递推
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f=[0]*len(nums)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[:i]):
                if x>y:
                    f[i]=max(f[i],f[j])
            f[i]+=1 # 递推里面无return # 大循环
        return max(f)

# 方法3：贪心+二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g=[]
        for x in nums:
            j=bisect_left(g,x) # g第一个大于等于x的值在g中索引
            if j==len(g):
                g.append(x)
            else:
                g[j]=x
        return len(g)

# 方法4：原地 贪心+二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng=0
        for x in nums:
            j=bisect_left(nums,x,0,ng)
            nums[j]=x # 就是把nums当作g数组了
            if j==ng:
                ng+=1
        return ng