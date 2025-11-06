# 739. Daily Temperatures

# 方法1：从右往左：维护递减栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            t=temperatures[i]
            while st and t>=temperatures[st[-1]]: # 大于等于就可以弹出了 # 比温度
                st.pop()
            if st:
                ans[i]=st[-1]-i
            st.append(i)
        return ans

# 方法2：从左往右：维护递增栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i,t in enumerate(temperatures):
            while st and t>temperatures[st[-1]]:
                j=st.pop()
                ans[j]=i-j
            st.append(i)
        return ans