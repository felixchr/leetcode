from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for i in nums:
            if sum > 0:
                sum += i
            else:
                sum = i
            ans = max(ans, sum)
        return ans

def test_args():
    s = Solution()
    func = s.maxSubArray
    test_cases = (
        (([-2,1,-3,4,-1,2,1,-5,4],), 6),
        (([1],), 1),
        (([5,4,-1,7,8],), 23),
    )
    return func, test_cases