# 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[0]*(n-k+1)
        q=deque()
        for i,x in enumerate(nums):
            while q and x>nums[q[-1]]: # 注意用while
                q.pop()
            q.append(i)
            left=i-k+1
            if q[0]<left: # append后不用考虑非空了
                q.popleft()
            if left>=0:
                ans[left]=nums[q[0]] # 最后注意这个数组的索引
        return ans