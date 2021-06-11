# from memory_profiler import profile
from math import log10, floor
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        stack = []
        while(x):
            stack.append(x % 10)
            x = x // 10
        for i in range(len(stack)//2):
            if stack[i] != stack[-1 - i]:
                return False
        else:
            return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        x_str = str(x)
        for i in range(len(x_str)//2):
            if x_str[i] != x_str[-1 - i]:
                return False
        else:
            return True

class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        # n_digt = int(log10(x))
        # r = 1 if n_digt % 2 else 10
        tmp_x = x
        new_x = 0
        while tmp_x >= new_x * 10:
            print(tmp_x, new_x)
            new_tmp = tmp_x // 10
            if new_tmp == new_x:
                return True
            new_x = new_x * 10 + tmp_x % 10
            if new_x == 0:
                return False
            if new_tmp == new_x:
                return True
            tmp_x = new_tmp
        else:
            return False

class Solution4:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        n_digt = int(log10(x))
        tmp_x = x
        while tmp_x >= 10:
            power_of_ten = 10 ** n_digt
            left = tmp_x // power_of_ten
            right = tmp_x % 10
            if left != right:
                return False
            reminder = (tmp_x % power_of_ten) // 10 
            if reminder < (power_of_ten // 10):
                return False
            tmp_x = reminder
            n_digt -= 2
            if n_digt <= 0:
                return True
        return True

class Solution5:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        a, b = x, 0
        while a >= b:
            if a == b:
                return True
            reminder = a % 10
            a = a // 10
            if a == 0:
                return False
            if a == b:
                return True
            b = b * 10 + reminder
        return False


# @profile
def test_solution():
    s = Solution3()
    try:
        for number, result in ((1221, True), (121, True), (10, False), (100021, False), (-121, False),
                (11, True), (1001, True), (313, True), (101, True)):
            assert s.isPalindrome(number) == result
    except Exception as e:
        print('The wrong number is: {}'.format(number))
        return 'Failed'
    else:
        return 'Passed'

def test_args():
    s = Solution5()
    func = s.isPalindrome
    test_cases = (
        (1221, True), 
        (121, True), 
        (10, False), 
        (100021, False), 
        (-121, False),
        (11, True),
        (1001, True),
        (313, True),
        (101, True),
        (21120, False)
    )
    return func, test_cases