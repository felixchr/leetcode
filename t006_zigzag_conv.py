class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        lines = [[] for _ in range(numRows)]
        numPerGrp = numRows * 2 - 2
        for i, c in enumerate(s):
            # print(i, c)
            mod = i % numPerGrp
            if mod < numRows:
                row = mod
            else:
                row = numPerGrp - mod
            lines[row].append(c)
            # print(lines)
        return ''.join([''.join(l) for l in lines])

class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        ret = [''] * len(s)
        numPerGrp = numRows * 2 - 2
        for i, c in enumerate(s):
            mod = i % numPerGrp
            noGrp = i // numPerGrp
            if mod < numRows:
                index = noGrp * numPerGrp + mod
            else:
                index = noGrp * numPerGrp


def test_args():
    s = Solution()
    func = s.convert
    test_cases = (
        (('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR'),
        (('PAYPALISHIRING', 4), 'PINALSIGYAHRPI'),
        (('', 1), ''),
        (('A', 1), 'A'),
        (('AB', 1), 'AB')
    )
    return func, test_cases