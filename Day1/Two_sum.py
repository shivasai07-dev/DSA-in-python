class Solution(object):
    def twoSum(self, nums, target):
        
        if not nums:  
            return None
        
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None  

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))