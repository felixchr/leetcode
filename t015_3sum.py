from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find out the triplets that sums equals 0

        :param nums: list of integers
        :return: list of triplets
        """
        length = len(nums)
        if length < 3:
            return []
        ret = []
        nums.sort()
        # print(nums)
        for left in range(length-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = length - 1
            while mid < right:
                current_sum = nums[left] + nums[mid] + nums[right]
                if current_sum < 0:
                    mid += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # print(left, mid, right)
                    ret.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
                    # print(left, mid, right)
        return ret

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        ret = []
        for i in range(0, length):
            for j in range(i+1, length):
                num_desired = 0 - (nums[i] + nums[j])
                try:
                    k = nums[j+1:].index(num_desired)
                except ValueError:
                    continue
                print(i, j, k+j+1)
                tmp_solution = [nums[i], nums[j], nums[k+j+1]]
                tmp_solution.sort()
                if tmp_solution not in ret:
                    ret.append(tmp_solution)
        return ret

def test_args():
    s = Solution()
    func = s.threeSum
    test_cases = (
        (([-1,0,1,2,-1,-4],), [[-1,-1,2],[-1,0,1]]),
        (([],), []),
        (([0],), []),
    )
    return func, test_cases