from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lead = 0
        l = len(nums)
        if l == 0:
            return 0
        while l > 1:
            idx = l // 2
            print(l, lead, idx)
            if nums[idx + lead] == target:
                return idx + lead
            elif target < nums[idx + lead]:
                # to the left
                l = idx
            else:
                # to the right
                lead += idx
                l = l - idx
        else:
            if nums[lead] == target:
                return lead
            elif target < nums[lead]:
                return lead
            else:
                return lead + 1

def test_solution():
    s = Solution()
    test_cases = (
        (([1,3,5,6], 5), 2),
        (([1,3,5,6], 2), 1),
        (([1,3,5,6], 7), 4),
        (([1,3,5,6], 0), 0),
    )
    for ins, out in test_cases:
        if s.searchInsert(*ins) != out:
            print(ins, out)
            print('Failed!')
            break
    else:
        print('Passed!')
            