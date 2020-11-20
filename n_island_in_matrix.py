from typing import List
class Solution:
    def n_island_in_matrix(self, matrix: List) -> int:
        def digonal_point(x, y):
            r_x = 1 if x == 0 else 0
            r_y = 1 if y == 0 else 0
            return (r_x, r_y)
        def adjacent_point(x, y):
            ret = []
            x1 = 1 if x == 0 else 0
            ret.append((x1, y))
            y1 = 1 if y == 0 else 0
            ret.append((x, y1))
            return ret
        for y in range(2):
            for x in range(2):
                if matrix[x][y] == 1:
                    if y == 1:
                        return 1
                    for x1, y1 in adjacent_point(x, y):
                        if matrix[x1][y1] == 1:
                            return 1
                    else:
                        x1, y1 = digonal_point(x, y)
                        if matrix[x1][y1] == 1:
                            return 2
                        else:
                            return 1
        else:
            return 0

def test_solution():
    s = Solution()
    test_cases = (
        (((0, 1), (1, 0)), 2),
        (((0, 1), (1, 1)), 1),
        (((0, 1), (0, 0)), 1),
        (((0, 0), (0, 0)), 0),
        (((1, 1), (1, 1)), 1),
        (((1, 0), (0, 1)), 2),
        (((1, 1), (1, 0)), 1),
        (((0, 0), (1, 0)), 1),
        (((0, 0), (0, 1)), 1)
    )
    for matrix, ans in test_cases:
        ret = s.n_island_in_matrix(matrix)
        if ret != ans:
            print('Failed!')
            print(matrix, ans, ret)
            break
    else:
        print('Passed!')
