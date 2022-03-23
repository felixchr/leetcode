class Solution:
    def intToRoman(self, num: int) -> str:
        iToRTuple = (
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        )
        tmpNum = num
        ret = ''
        # while tmpNum > 0:
        for xnum, rchar in iToRTuple:
            while tmpNum >= xnum:
                ret += rchar
                tmpNum = tmpNum - xnum
            if tmpNum == 0:
                break
        return ret
                
def test_args():
    s = Solution()
    func = s.intToRoman
    test_cases = (
        (3, 'III'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV'),
    )
    return func, test_cases