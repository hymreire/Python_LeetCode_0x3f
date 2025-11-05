# 337. House Robber III

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node): # 返回当前节点抢的最大值和不抢的最大值
            if node==None:
                return 0,0
            l,l_not=dfs(node.left)
            r,r_not=dfs(node.right)
            rob=node.val+l_not+r_not
            not_rob=max(l,l_not)+max(r,r_not)
            return rob,not_rob
        return max(dfs(root))