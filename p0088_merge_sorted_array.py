from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        if m == 0:
            for i, num in enumerate(nums2):
                nums1[i] = num
            return nums1
        ptr1 = -n-1
        ptr2 = -1
        for i in range(m+n):
            print(ptr1, ptr2, nums1)
            if ptr2 < -n:
                break
            if ptr1 < -m-n:
                nums1[-i-1] = nums2[ptr2]
                ptr2 -= 1
                continue
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[-i-1] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[-i-1] = nums2[ptr2]
                ptr2 -= 1
        return nums1

def test_args():
    s = Solution()
    func = s.merge
    test_cases = (
        (([2, 0], 1, [1], 1), [1, 2]),
        (([0], 0, [1], 1), [1]),
        (([1,2,3,0,0,0], 3, [2,5,6], 3), [1, 2, 2, 3, 5, 6])
    )
    return func, test_cases