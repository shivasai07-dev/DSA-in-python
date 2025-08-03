class Solution(object):
    def removeDuplicates(self, nums):
       
        if not nums:
            return 0

        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1

nums = [1, 1, 2]
solution = Solution()
new_length = solution.removeDuplicates(nums)
print(new_length)
print("nums =", nums[:new_length])