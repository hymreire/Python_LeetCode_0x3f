# 78. Subsets

# # 方法一：选或不选
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         ans=[]
#         path=[]

#         def dfs(i):
#             # 边界条件
#             if i==n:
#                 ans.append(path.copy()) # path全局变化，需存副本
#                 return
            
#             # 递降的两种选择：选或不选，两种情况一定都会出现
#             # 不选
#             dfs(i+1)
#             # 选，有选就有撤
#             path.append(nums[i])
#             dfs(i+1)
#             path.pop() # 恢复现场（撤销当前分支，恢复到上一个状态）

#         dfs(0)

#         return ans

# # 方法二：枚举选择
# # 方法二：枚举选择：从空集开始，按树状图形式添入
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n=len(nums)
#         ans=[]
#         path=[]

#         def dfs(i):
#             ans.append(path.copy())
#             for j in range(i,n):
#                 # 选择
#                 path.append(nums[j])
#                 # 递降
#                 dfs(j+1)
#                 path.pop() # 有选必有撤

#         dfs(0)

#         return ans


# ============= 调试版本 =============
def subsets_debug(nums):
    """带调试输出的版本，方便理解执行过程"""
    n = len(nums)
    ans = []
    path = []
    call_count = [0]  # 用列表存储，方便在内部函数修改
    
    def dfs(i, depth=0):
        call_count[0] += 1
        indent = "  " * depth  # 缩进表示递归深度
        
        # 1. 进入函数时的状态
        print(f"{indent}┌─ dfs({i}) 被调用，当前 path={path}")
        
        # 2. 收集答案
        ans.append(path.copy())
        print(f"{indent}│  ✓ 添加子集: {path.copy()}")
        
        # 3. 枚举下一步选择
        if i < n:
            print(f"{indent}│  开始枚举 range({i}, {n}): {list(range(i, n))}")
        
        for j in range(i, n):
            # 选择 nums[j]
            path.append(nums[j])
            print(f"{indent}│  → 选择 nums[{j}]={nums[j]}, path={path}")
            
            # 递归
            dfs(j + 1, depth + 1)
            
            # 撤销选择
            removed = path.pop()
            print(f"{indent}│  ← 撤销 nums[{j}]={removed}, path={path}")
        
        # 4. 函数返回
        print(f"{indent}└─ dfs({i}) 返回")
        print()
    
    print("=" * 60)
    print(f"开始执行: nums = {nums}")
    print("=" * 60)
    print()
    
    dfs(0)
    
    print("=" * 60)
    print(f"执行完成！共调用 dfs {call_count[0]} 次")
    print(f"最终答案: {ans}")
    print(f"子集总数: {len(ans)}")
    print("=" * 60)
    
    return ans


# ============= 测试代码 =============
if __name__ == "__main__":
    print("\n【测试 1】nums = [1, 2, 3]")
    result1 = subsets_debug([1, 2, 3])
    
    print("\n\n" + "=" * 80 + "\n\n")
    
    print("\n【测试 2】nums = [1, 2]")
    result2 = subsets_debug([1, 2])
    
    print("\n\n" + "=" * 80 + "\n\n")
    
    print("\n【测试 3】nums = [0]")
    result3 = subsets_debug([0])