from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = sorted(points, key=lambda p: p[0]*p[0] + p[1]*p[1])[:K]
        return result


def test_solution():
    s = Solution()
    test_cases = (([[1,3],[-2,2]], 1, [[-2, 2]]),
        ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]))
    for points, k, answer in test_cases:
        result = s.kClosest(points, k)
        if result != answer:
            print('Failed')
            print(points, answer, result)
            break
    else:
        print('Passed!')