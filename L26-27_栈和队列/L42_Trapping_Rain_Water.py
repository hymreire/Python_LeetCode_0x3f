# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        st=[]
        for i,h in enumerate(height):
            while st and h>=height[st[-1]]: # 注意用大于等于号，一旦大于等于后，靠右的边界能提供更大的收益
                j=st.pop()
                if not st: # 注意[]!=None
                    break
                bottom=i-st[-1]-1
                hei=min(h,height[st[-1]])-height[j]
                ans+=bottom*hei
            st.append(i)
        return ans