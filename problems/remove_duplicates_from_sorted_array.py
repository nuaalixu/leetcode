#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[slow] != nums[fast]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0
