from typing import List
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        value_hash = {}
        ret = []
        for i, num in enumerate(nums):
            value_hash.setdefault(num, []).append(i)
        for i, num1 in enumerate(nums):
            for j, num2  in enumerate(nums[i+1:], i+1):
                num3 = 0 - num1 - num2
                if num3 in value_hash:
                    l_num3_hash = len(value_hash[num3])
                    if l_num3_hash > 2 or (l_num3_hash == 2 and num1 != num2) or (l_num3_hash == 1 and i not in value_hash[num3] and j not in value_hash[num3]):
                        set_found = [num1, num2, num3]
                        set_found.sort()
                        if set_found not in ret:
                            ret.append(set_found)
                    else:
                        continue
        return ret

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        negative_list = [i for i in nums if i < 0]
        positive_list = [i for i in nums if i >= 0]
        ret = []
        for group1, group2 in ((negative_list, positive_list), (positive_list, negative_list)):
            for i, num1 in enumerate(group1):
                for j, num2 in enumerate(group1[i+1], i+1):
                    num3 = 0 - num1 - num2
                    if num3 in group2:
                        set_found = [num1, num2, num3]
                        set_found.sort()
                        if set_found not in ret:
                            ret.append(set_found)
        return ret






def test_solution():
    s = Solution()
    test_cases = (
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([1,2,-2,-1], [])
    )
    for in_list, out_list in test_cases:
        out = s.threeSum(in_list)
        if out != out_list:
            print(in_list, out)
            print('Failed!')
            break
    else:
        print('Passed!')