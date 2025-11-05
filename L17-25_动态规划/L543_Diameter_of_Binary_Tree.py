# 543. Diameter of Binary Tree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            if node==None:
                return -1 # 因为后面+1
            ll=dfs(node.left)+1
            lr=dfs(node.right)+1
            nonlocal ans
            ans=max(ans,ll+lr)
            return max(ll,lr)
        dfs(root)
        return ans