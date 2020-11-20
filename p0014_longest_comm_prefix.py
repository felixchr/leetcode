from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ret = []
        min_len = min([len(s) for s in strs])
        if min_len == 0:
            return ''
        i = 0
        while i < min_len:
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return ''.join(ret)
            else:
                ret.append(char)
            i += 1
        return ''.join(ret)

def test_solution():
    s = Solution()
    test_cases = (
        (['aca', 'cba'], ''),
        (["flower","flow","flight"], 'fl'),
        ([], '')
    )
    for in_list, out_str in test_cases:
        ret = s.longestCommonPrefix(in_list)
        if ret != out_str:
            print(in_list, ret, out_str)
            print('Failed!')
            break
    else:
        print('Passed!')
