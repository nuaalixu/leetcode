class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _map = dict()
        for index, num in enumerate(nums):
            quest = target - num
            if quest in _map:
                return _map[quest], index
            else:
                _map[num] = index
        return None
