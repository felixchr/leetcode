from typing import List
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        for i, num in enumerate(height):
            for j in range(i+1, len(height)):
                h = num if num <= height[j] else height[j]
                w = j - i
                area = h * w
                maxA = area if area > maxA else maxA
        return maxA

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        indexLeft = 0
        indexRight = len(height) - 1
        while indexLeft < indexRight:
            maxarea = max(maxarea, min(height[indexLeft], height[indexRight]) * (indexRight - indexLeft))
            if height[indexLeft] < height[indexRight]:
                indexLeft += 1
            else:
                indexRight -= 1
        return maxarea


def test_solution():
    s = Solution()
    test_cases = (
        ([1,8,6,2,5,4,8,3,7], 49),

    )
    for in_list, expected_out in test_cases:
        area = s.maxArea(in_list)
        if area != expected_out:
            print(in_list, expected_out, area)
            print('Failed!')
            break
        else:
            print('Passed')