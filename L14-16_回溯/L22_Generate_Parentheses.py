# 22. Generate Parentheses

# 方法一：选或不选
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m=2*n # 括号总数
        ans=[]
        path=[""]*m # 存储当前组合
        # 输入左右括号个数，输出剩余位置合法的path
        def dfs(l,r):
            # 边界条件：右括号数量为n（前提是约束左右括号不越界）
            if r==n:
                ans.append("".join(path))
                return
            if l<n: # 约束条件，左括号不得大于n
                path[l+r]="("
                dfs(l+1,r)
            if r<l: # 约束条件，右括号不得大于左括号
                path[l+r]=")" # 思考一下：覆盖等价于不选左括号吗？
                dfs(l,r+1)
        dfs(0,0)
        return ans

# 方法二：枚举选择
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=[] # 记录左括号下标，因此本题不涉及右括号直接操作
        # 输入：当前括号总数，输出左右括号差值
        def dfs(i,d):
            # 边界条件：左括号位置完全确定
            if len(path)==n:
                s=[")"]*(2*n)
                for j in path:
                    s[j]="("
                ans.append("".join(s))
                return # 一定要return终止，否则递降不会结束
            # 枚举选择：差值就是可选右括号数量，遍历
            # 本题不涉及右括号直接操作，确定左括号索引即可实现等价效果
            # 一次只处理一个左括号索引不会乱
            for r in range(d+1):
                path.append(i+r)
                dfs(i+r+1,d-r+1)
                path.pop()
        dfs(0,0)
        return ans