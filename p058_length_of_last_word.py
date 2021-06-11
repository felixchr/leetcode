class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        ret = 0
        for char in s[::-1]:
            if char == ' ':
                if ret == 0:
                    continue
                else:
                    return ret
            else:
                ret += 1
        return ret

def test_args():
    s = Solution()
    func = s.lengthOfLastWord
    test_cases = (
        ("Hello World", 5),
        (" ", 0),
        ("a ", 1),
    )
    return func, test_cases
            