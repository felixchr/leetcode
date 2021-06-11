class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        middle = left + (right - left) // 2
        while left < right and left < middle:
            power_left = left * left
            power_right = right * right
            power_middle = middle * middle
            if power_middle == x:
                return middle
            elif power_left < x < power_middle:
                right = middle
                middle = left + (right - left) // 2
            elif power_middle < x < power_right:
                left = middle
                middle  = left + (right - left) // 2
            else:
                return right
        return middle

class Solution2:
    def mySqrt(self, x: int) -> int:
        if x <= 3:
            return 1
        left, right = 1, x
        while left < right:
            middle = left + (right - left)//2
            power_of_middle = middle * middle
            if power_of_middle == x:
                return middle
            elif power_of_middle < x:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1
        return ans


def test_args():
    s = Solution2()
    func = s.mySqrt
    test_cases = (
        (4, 2),
        (8, 2),
        (1, 1),
        (9, 3)
    )
    return func, test_cases