import re
class Solution1:
    def reverse(self, x: int) -> int:
        p = re.compile(r'([-]?)(\d+)')
        sign, num = p.findall(str(x))[0]
        new_num = num[::-1]
        ret = int('{}{}'.format(sign, new_num))
        return ret if -2**31 <= ret <= 2**31 else 0
    
class Solution0:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        new_x = abs(x)
        sign = -1 if x < 0 else 1
        ret = 0
        max_num = 1<<31
        while new_x:
            reminder = new_x % 10
            ret = 10 * ret + reminder
            new_x = new_x // 10
            if ret >= max_num:
                return 0
        ret = ret * sign
        return ret
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x < 0:
            sign = -1
        else:
            sign = 1
        new_num = int(str(x * sign)[::-1]) * sign
        return new_num if -2**31 <= new_num <= 2**31 else 0

class Solution2:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        abs_x = abs(x)
        new_x = 0
        while abs_x >= 10:
            reminder = abs_x % 10
            new_x = new_x * 10 + reminder
            abs_x = abs_x // 10
        new_x = new_x * 10 + abs_x
        if new_x > 2**31:
            return 0
        return new_x * sign



def test_args():
    s = Solution2()
    func = s.reverse
    test_cases = (
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (10, 1)
    )
    return func, test_cases