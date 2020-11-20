class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int('0b{}'.format(a), 2) + int('0b{}'.format(b), 2))[2:]

class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        def _string_add(s1, s2, s3):
            # should be all '0' and '1'
            s = sum([1 for n in (s1, s2, s3) if n == '1'])
            carry_bit = '1' if s >= 2 else '0'
            left_bit = '0' if s == 2 or s == 0 else '1'
            return left_bit, carry_bit
        ret = []
        l_a, l_b = len(a), len(b)
        if l_a <= l_b:
            c, d = a, b
            s_l, l_l = l_a, l_b
        else:
            c, d = b, a
            s_l, l_l = l_b, l_a
        carry_bit = '0'
        for i in range(1, l_l+1):
            e = c[-i] if i < s_l + 1 else '0'
            print(e, d[-i], carry_bit)
            left_bit, carry_bit = _string_add(e, d[-i], carry_bit)
            ret.insert(0, left_bit)
        if carry_bit != '0':
            ret.insert(0, '1')
        return ''.join(ret)

def test_solution():
    s = Solution2()
    test_cases = (
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
        ('0', '0', '0')
    )
    for a, b, answer in test_cases:
        print('Testing {} + {}'.format(a, b))
        ret = s.addBinary(a, b)
        if ret != answer:
            print('Failed')
            print(a, b, answer, ret)
            break
    else:
        print('Passed!')