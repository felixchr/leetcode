import re
class Solution1:
    def reverse(self, x: int) -> int:
        p = re.compile(r'([-]?)(\d+)')
        sign, num = p.findall(str(x))[0]
        new_num = num[::-1]
        ret = int('{}{}'.format(sign, new_num))
        return ret if -2**31 <= ret <= 2**31 else 0
    
class Solution:
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