# 124. Binary Tree Maximum Path Sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-inf
        def dfs(node):
            if node==None:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            nonlocal ans
            ans=max(ans,l+r+node.val)
            return max(max(l,r)+node.val,0) # 左链和右链最大值，小于0直接不选（空集）
        dfs(root)
        return ans