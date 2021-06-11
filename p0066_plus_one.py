from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        to_add = 1
        for i in range(1, length + 1):
            if to_add == 0:
                break
            sum = digits[-i] + to_add
            if sum == 10:
                to_add = 1
                digits[-i] = 0
            else:
                digits[-i] = sum
                to_add = 0
        else:
            if to_add == 1:
                digits.insert(0, 1)
        return digits

def test_args():
    s = Solution()
    func = s.plusOne
    test_cases = (
        (([1,2,3],), [1,2,4]),
        (([4,3,2,1],), [4,3,2,2]),
        (([0],), [1]),
        (([9],), [1, 0])
    )
    return func, test_cases
