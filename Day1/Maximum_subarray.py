class Solution(object):
    def maxSubArray(self, nums): 
        if not nums:
            return 0
        maxsub = nums[0]
        currsub = 0
        for right in nums:
            if currsub < 0:
                currsub = 0
            currsub += right
            maxsub = max(currsub, maxsub)
        return maxsub 

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(nums))