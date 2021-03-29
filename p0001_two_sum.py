class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            rest = target - nums[i]
            if rest in nums[i+1:]:
                return [i, nums[i+1:].index(rest) + i + 1]

def test_args():
    s = Solution()
    func = s.twoSum
    test_cases = (
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1])
    )
    return func, test_cases