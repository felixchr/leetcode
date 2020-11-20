from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i)
                continue
            i += 1
        return len(nums)

def test_solution():
    s = Solution()
    test_cases = (
        ([1, 1, 2], 2, [1, 2]),
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4])
    )
    for in_list, ret_len, ret_list in test_cases:
        num = s.removeDuplicates(in_list)
        if ret_len != num or in_list != ret_list:
            print(in_list, ret_len, num)
            print('Failed!')
            break
    else:
        print('Passed!')