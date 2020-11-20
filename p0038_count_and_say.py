class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ret = ''
        t_s = self.countAndSay(n-1)
        t_ch = t_s[0]
        t_n = 1
        for ch in t_s[1:]:
            if ch == t_ch:
                t_n += 1
            else:
                ret = f'{ret}{t_n}{t_ch}'
                t_n = 1
                t_ch = ch
        ret = f'{ret}{t_n}{t_ch}'
        return ret

def test_solution():
    s = Solution()
    test_cases = (
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
        (5, '111221'),
        (6, '312211'),
        (7, '13112221'),
        (8, '1113213211'),
        (9, '31131211131221'),
        (10, '13211311123113112211')
    )
    for ins, out in test_cases:
        ret = s.countAndSay(ins)
        if ret != out:
            print(ins, out, ret)
            print('Failed!')
            break
    else:
        print('Passed!')