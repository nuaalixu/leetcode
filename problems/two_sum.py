def two_sum_naive(nums, target):
    '''
    暴力搜索，for循环两次，O(n^2)
    '''
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if target == nums[i] + nums[k]:
                return i, k
        return None

def two_sum_faster(nums, target):
    '''
    因为dict结构，搜索是O(1),所以最终O(n)
    '''
    _map = dict()
    for index, num in enumerate(nums):
        quest = target - num
        if quest in _map:
            return _map[quest], index
        else:
            _map[num] = index
    return None

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_naive(nums, target))
    print(two_sum_faster(nums, target))
