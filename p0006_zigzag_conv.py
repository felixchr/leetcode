class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l_s = len(s)
        if numRows == 1 or l_s <= numRows:
            return s
        numCols = l_s // numRows
        lines = [[] for _ in range(numRows)]
        nOfGroup = 2 * numRows - 2
        for i in range(l_s // nOfGroup + 1):
            for row in range(numRows):
                index = i * nOfGroup + row
                if index >= l_s:
                    return ''.join(''.join([ c for c in line]).strip() for line in lines )
                lines[row].append(s[index])
                # print(index, lines)
            for col in range(numRows - 2):
                index = i * nOfGroup + numRows + col
                if index >= l_s:
                    return ''.join(''.join([ c for c in line]).strip() for line in lines )
                lines[numRows - col - 2].append(s[index])
                # for row in range(numRows):
                #     if row == :
                #         lines[row].append(s[index])
                    # else:
                    #     lines[row].append(' ')

def test_solution():
    s = Solution()
    test_cases = (
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
        ('', 1, ''),
        ('A', 1, 'A'),
        ('AB', 1, 'AB')
    )
    for in_str, numRows, ret in test_cases:
        out = s.convert(in_str, numRows)
        if out != ret:
            print(in_str, numRows)
            print(ret)
            print(out)
            print('Failed!')
            break
    else:
        print('Passed')

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